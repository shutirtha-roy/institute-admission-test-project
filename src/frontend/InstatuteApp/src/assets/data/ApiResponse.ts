import { IApiResponse, IResult } from "./IApiResponse";

export class ApiResponse implements IApiResponse {
    public success!: string;
    public message!: string;
    public data!: IResult;

    public constructor(init?:Partial<ApiResponse>) {
        Object.assign(this, init);
    }
}