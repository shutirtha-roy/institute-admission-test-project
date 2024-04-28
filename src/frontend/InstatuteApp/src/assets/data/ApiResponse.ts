import { IApiResponse, IResult } from "./IApiResponse";

export class ApiResponse implements IApiResponse {
    public id!: string;
    public statuscode!: string;
    public errormessages!: string[];
    public result!: IResult;

    public constructor(init?:Partial<ApiResponse>) {
        Object.assign(this, init);
    }
}