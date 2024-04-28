export interface IApiResponse {
    id: string,
    statuscode: string,
    errormessages: string[],
    result: IResult
}

export interface IResult {
    token: string;
    user: IUser;
} 

export interface IUser {
    id: string,
    name: string,
    password: string,
    role: string,
    userName: string
}