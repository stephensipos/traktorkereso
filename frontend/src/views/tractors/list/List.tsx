import React, { useState, useEffect } from 'react';
import { makeStyles, createStyles, Theme } from '@material-ui/core/styles';
import Grid, { GridSpacing } from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';

import Item from "./Item"
import axios from 'axios';

const useStyles = makeStyles((theme: Theme) =>
	createStyles({
		root: {
			flexGrow: 1,
		},
		paper: {
			height: 140,
			width: 100,
		},
		control: {
			padding: theme.spacing(2),
		},
	}),
);

export default function Tractors() {
	const classes = useStyles()
	const [tractors, setTractors] = useState([])

	useEffect(() => {
		axios({
			method: "get",
			url: `${process.env.REACT_APP_API_BASE_URL}/tractors`,
		})
			.then(response => {
				if (response.data?.tractors) {
					setTractors(response.data.tractors)
				}
			})
			.catch(error => {
				console.log(error)
			})
	}, [])

	return (
		<Grid container className={classes.root} spacing={2}>
			<Grid item xs={12}>
				<Grid container justify="center" spacing={3}>
					{tractors.map((tractor) => (
						<Grid item>
							<Item tractor={tractor} />
						</Grid>
					))}
				</Grid>
			</Grid>
		</Grid>
	);
}