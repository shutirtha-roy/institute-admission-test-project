from uuid import UUID
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp
from fastapi import Request
from fastapi.responses import JSONResponse

from userRole.model import UserRole
import re


class AuthorizationMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp, skip_endpoints: list = []) -> None:
        super().__init__(app, self.dispatch)
        self.url = "/api/v1"
        self.skip_endpoints = skip_endpoints

    async def dispatch(self, request: Request, call_next):
        endpoint = str(request.url)[len(str(request.base_url))-1:]

        if endpoint[:len(self.url)] == self.url:
            endpoint = endpoint[len(self.url):]

        for skip in self.skip_endpoints:
            if request.method == skip["method"] and re.search(skip["regex"], endpoint):
                return await call_next(request)

        if "organization" in request.headers:
            user_role = await UserRole.find_one(UserRole.user.id == UUID(request.state.user), fetch_links=True)
            
            if user_role is not None:
                request.state.organization = user_role.organization
                request.state.role = user_role.role
                request.state.employee_id = user_role.employee_id

            return await call_next(request)
        else:
            return JSONResponse(status_code=403, content={"success": False, "message": "User is not authorized to access this Organization"})