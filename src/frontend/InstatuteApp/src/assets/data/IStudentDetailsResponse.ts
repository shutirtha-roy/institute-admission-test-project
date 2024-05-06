export interface IStudentDetailsResponse {
    success: string,
    message: string,
    result: IStudentResult
}

export interface IStudentResult {
    total_students: number,
    studentt_list: IStudent[]
}

export interface IStudent {
    _id: string,
    password: string,
    role: string,
    name: string,
    email: string,
    approved: boolean
}