import { IStudentResult, IStudentDetailsResponse } from "./IStudentDetailsResponse";


export class StudentDetailsResponse implements IStudentDetailsResponse {
    public success!: string;
    public message!: string;
    public result!: IStudentResult;

    public constructor(init?:Partial<StudentDetailsResponse>) {
        Object.assign(this, init);
    }
}