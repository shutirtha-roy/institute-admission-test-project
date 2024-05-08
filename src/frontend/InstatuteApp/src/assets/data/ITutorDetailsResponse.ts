export interface ITutorDetailsResponse {
    success: string,
    message: string,
    result: ITutorResult
}

export interface ITutorResult {
    total_tutors: number,
    tutor_list: ITutor[]
}

export interface ITutor {
    _id: string,
    password: string,
    role: string,
    name: string,
    email: string,
    approved: boolean
}