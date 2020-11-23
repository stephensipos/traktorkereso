import { combineReducers } from "redux"
import { userAuthenticated } from "./actions"


export type UserReducerInitialState = {
	isAuthenticated: boolean,
	token: null | string,
	profile: any,
}
export const userReducerInitialState: UserReducerInitialState = {
	isAuthenticated: false,
	token: null,
	profile: null,
}
type UserReducerAction = ReturnType<typeof userAuthenticated>
const userReducer = (state: UserReducerInitialState = userReducerInitialState, action: UserReducerAction): UserReducerInitialState => {
	switch (action.type) {
		case "USER_AUTHENTICATED": {
			return {
				...state,
				isAuthenticated: true,
				token: action.payload.token,
			}
		}

		default: {
			return state
		}
	}
}


export const rootReducer = combineReducers({
	user: userReducer,
})

