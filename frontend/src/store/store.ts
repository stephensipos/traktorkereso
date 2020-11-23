import { createStore } from "redux"
import { rootReducer } from "./reducers"
import { composeWithDevTools } from "redux-devtools-extension"
import { userReducerInitialState } from "./reducers"

const defaultState = {
	user: userReducerInitialState,
}

export const store = createStore(
	rootReducer,
	defaultState,
	composeWithDevTools(),
)
