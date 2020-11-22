import React, { useState } from "react"
import Avatar from "@material-ui/core/Avatar"
import Button from "@material-ui/core/Button"
import CssBaseline from "@material-ui/core/CssBaseline"
import TextField from "@material-ui/core/TextField"
import Grid from "@material-ui/core/Grid"
import LockOutlinedIcon from "@material-ui/icons/LockOutlined"
import Typography from "@material-ui/core/Typography"
import Container from "@material-ui/core/Container"
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { makeStyles } from "@material-ui/core/styles"
import axios from "axios"
import { useHistory } from "react-router-dom"

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

export default function SignUp() {
	const classes = useStyles()
	const history = useHistory()
	const [fieldErrors, setFieldErrors] = useState<{ [key: string]: string }>({})
	const [successDialogVisible, setSuccessDialogVisible] = useState<boolean>(false)

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
			url: `${process.env.REACT_APP_API_BASE_URL}/register`,
			data: {
				username: formFields.username,
				password: formFields.password,
				email: formFields.email,
				first_name: formFields.firstName,
				last_name: formFields.lastName,
			},
		})
			.then(response => {
				if (response.status === 201) {
					setSuccessDialogVisible(true)
				}
			})
			.catch(error => {
				if (error.response.status === 409) {
					if (error.response.data.error_code === 1) {
						setFieldErrors({
							username: "This username is already taken"
						})
					}
					else if (error.response.data.error_code === 2) {
						setFieldErrors({
							email: "This email address is already use"
						})
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

		if (fields.hasOwnProperty("firstName")) {
			if (fields["firstName"].length === 0) {
				errors["firstName"] = "This field is required"
			}
		}

		if (fields.hasOwnProperty("lastName")) {
			if (fields["lastName"].length === 0) {
				errors["lastName"] = "This field is required"
			}
		}

		if (fields.hasOwnProperty("email")) {
			if (fields["email"].length === 0) {
				errors["email"] = "This field is required"
			}
		}

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

	const onSuccessDialogClose = (): void => {
		history.push("/login")
	}

	return (
		<React.Fragment>
			<Dialog
				open={successDialogVisible}
				onClose={onSuccessDialogClose}
				aria-labelledby="alert-dialog-title"
				aria-describedby="alert-dialog-description"
			>
				<DialogTitle id="alert-dialog-title">Registration successful</DialogTitle>

				<DialogContent>
					<DialogContentText id="alert-dialog-description">
						You successfully registered. Now you can log in. 😊
					</DialogContentText>
				</DialogContent>

				<DialogActions>
					<Button onClick={onSuccessDialogClose} color="primary" autoFocus>Okay</Button>
				</DialogActions>
			</Dialog>

			<Container component="main" maxWidth="xs">
				<CssBaseline />
				<div className={classes.paper}>
					<Avatar className={classes.avatar}>
						<LockOutlinedIcon />
					</Avatar>

					<Typography component="h1" variant="h5">
						Sign up
				</Typography>

					<form className={classes.form} noValidate onSubmit={onSubmit}>
						<Grid container spacing={2}>
							<Grid item xs={12} sm={6}>
								<TextField
									name="firstName"
									variant="outlined"
									required
									fullWidth
									id="firstName"
									label="First Name"
									autoFocus
									error={fieldErrors.hasOwnProperty("firstName")}
									helperText={fieldErrors.hasOwnProperty("firstName") && fieldErrors["firstName"]}
								/>
							</Grid>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="lastName"
									label="Last Name"
									name="lastName"
									error={fieldErrors.hasOwnProperty("lastName")}
									helperText={fieldErrors.hasOwnProperty("lastName") && fieldErrors["lastName"]}
								/>
							</Grid>
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
									id="email"
									label="Email Address"
									name="email"
									error={fieldErrors.hasOwnProperty("email")}
									helperText={fieldErrors.hasOwnProperty("email") && fieldErrors["email"]}
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
						</Grid>
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
						>
							Sign Up
					</Button>
					</form>
				</div>
			</Container>
		</React.Fragment>
	)
}