import React, { useState } from "react"
import Container from "@material-ui/core/Container"
import CssBaseline from "@material-ui/core/CssBaseline"
import { makeStyles } from "@material-ui/core/styles"
import Avatar from "@material-ui/core/Avatar"
import LockOutlinedIcon from "@material-ui/icons/LockOutlined"
import WarningOutlinedIcon from "@material-ui/icons/WarningOutlined"
import Typography from "@material-ui/core/Typography"
import Button from "@material-ui/core/Button"
import TextField from "@material-ui/core/TextField"
import Grid from "@material-ui/core/Grid"
import Alert from "@material-ui/lab/Alert"
import axios from "axios"
import { useSelector, useDispatch } from "react-redux"
import { userAuthenticated } from "../../store/actions"

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: "flex",
		flexDirection: "column",
		alignItems: "center",
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main,
	},
	form: {
		width: "100%",
		marginTop: theme.spacing(3),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
}))


export default function Login() {
	const classes = useStyles()
	const [fieldErrors, setFieldErrors] = useState<{ [key: string]: string }>({})
	const [authenticationFailed, setAuthenticationFailed] = useState<boolean>(false)
	const dispatch = useDispatch()

	const onSubmit = (event: React.FormEvent): void => {
		event.preventDefault()

		let formData: FormData = new FormData(event.target as HTMLFormElement)
		let formFields: { [key: string]: any } = {}
		for (const [key, value] of Array.from(formData.entries())) {
			formFields[key] = value
		}

		let validatedFields: { [key: string]: string } = validateFields(formFields)
		if (Object.keys(validatedFields).length > 0) {
			setFieldErrors(validatedFields)
			return
		}
		else {
			setFieldErrors({})
		}

		axios({
			method: "post",
			url: `${process.env.REACT_APP_API_BASE_URL}/login`,
			data: {
				username: formFields.username,
				password: formFields.password,
			},
		})
			.then(response => {
				if (response.status === 200) {
					setAuthenticationFailed(false);

					dispatch(userAuthenticated({
						token: response.data.bearer,
					}))
				}
			})
			.catch(error => {
				if (error.response.status === 401) {
					if (error.response.data.error_code === 1) {
						setAuthenticationFailed(true);
					}
					else {
						alert("Unknown error code provided")
					}
				}
				else {
					alert("Unknown error occurred")
				}
			})

	}

	const validateFields = (fields: { [key: string]: any }): { [key: string]: string } => {
		let errors: { [key: string]: string } = {}

		if (fields.hasOwnProperty("username")) {
			if (fields["username"].length === 0) {
				errors["username"] = "This field is required"
			}
		}

		if (fields.hasOwnProperty("password")) {
			if (fields["password"].length === 0) {
				errors["password"] = "This field is required"
			}
		}

		return errors
	}

	const renderIcon = function () {
		if (authenticationFailed) {
			return (
				<WarningOutlinedIcon />
			)
		} else {
			return (
				<LockOutlinedIcon />
			)
		}
	}

	const renderTitle = function () {
		if (authenticationFailed) {
			return "Authentication failed!"
		} else {
			return "Sign up"
		}
	}

	const showAlert = function () {
		if (authenticationFailed) {
			return (
				<Grid item xs={12}>
					<Alert severity="error">Authentication failed!</Alert>
				</Grid>
			)
		}
	}
	return (
		<Container component="main" maxWidth="xs">
			<CssBaseline />
			<div className={classes.paper}>
				<Avatar className={classes.avatar}>
					<LockOutlinedIcon />
				</Avatar>
				<Typography component="h1" variant="h5">
					Log In!
                </Typography>

				<form className={classes.form} noValidate onSubmit={onSubmit}>
					<Grid container spacing={2}>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="username"
								label="Username"
								name="username"
								error={fieldErrors.hasOwnProperty("username")}
								helperText={fieldErrors.hasOwnProperty("username") && fieldErrors["username"]}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								name="password"
								label="Password"
								type="password"
								id="password"
								error={fieldErrors.hasOwnProperty("password")}
								helperText={fieldErrors.hasOwnProperty("password") && fieldErrors["password"]}
							/>
						</Grid>
						{showAlert()}
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
						>
							Sign Up
                        </Button>
					</Grid>
				</form>
			</div>
		</Container>
	)
}