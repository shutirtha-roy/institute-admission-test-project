export interface IApiResponse {
    success: string,
    message: string,
    data: IResult
}

export interface IResult {
    access_token: string;
    user: IUser;
} 

export interface IUser {
    name: string,
    email: string,
    role: string,
}