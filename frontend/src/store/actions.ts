type DispatchReturn<Type = string, Payload = any> = {
	type: Type,
	payload: Payload,
}


export type UserAuthenticatedPayload = {
	token: string,
}
export const userAuthenticated = (payload: UserAuthenticatedPayload): DispatchReturn<"USER_AUTHENTICATED", UserAuthenticatedPayload> => {
	return {
		type: "USER_AUTHENTICATED",
		payload: payload,
	}
}
