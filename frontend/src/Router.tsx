import React from "react";
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Link
} from "react-router-dom";

import RegisterView from "./views/auth/Register"
import LoginView from "./views/auth/Login"
import TractorListView from "./views/tractors/list/List"

export default () => {
	return (
		<Router>
			<div>
				<nav>
					<ul>
						<li>
							<Link to="/">traktorok (home)</Link>
						</li>
						<li>
							<Link to="/register">register</Link>
						</li>
						<li>
							<Link to="/login">login</Link>
						</li>
					</ul>
				</nav>

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