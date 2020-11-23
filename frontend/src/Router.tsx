import React from "react";
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Link
} from "react-router-dom";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';

import RegisterView from "./views/auth/Register"
import LoginView from "./views/auth/Login"
import TractorListView from "./views/tractors/list/List"

const useStyles = makeStyles((theme: Theme) =>
	createStyles({
		root: {
			flexGrow: 1,
			marginBottom: 30,
		},
		menuButton: {
			marginRight: theme.spacing(2),
		},
		title: {
			flexGrow: 1,
		},
	}),
);

export default () => {
	const classes = useStyles();
	return (
		<Router>
			<div>
				<div className={classes.root}>
					<AppBar position="static">
						<Toolbar>
							<Typography variant="h6" className={classes.title}>
								Traktorkereső
							</Typography>
							<Button color="inherit">
								<Link to="/" style={{color: "inherit", textDecoration: "none"}}>Traktorok</Link>
							</Button>
							<Button color="inherit">
								<Link to="/register" style={{color: "inherit", textDecoration: "none"}}>Register</Link>
							</Button>
							<Button color="inherit">
								<Link to="/login" style={{color: "inherit", textDecoration: "none"}}>Login</Link>
							</Button>
						</Toolbar>
					</AppBar>
				</div>

				<Switch>
					<Route path="/register">
						<RegisterView />
					</Route>
					<Route path="/login">
						<LoginView />
					</Route>
					<Route path="/">
						<TractorListView />
					</Route>
				</Switch>
			</div>
		</Router>
	);
}