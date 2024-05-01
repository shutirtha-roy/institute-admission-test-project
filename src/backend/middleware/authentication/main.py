import re

import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from .hash import ALGORITHM, SECRET_KEY


class AuthenticationMiddleware(BaseHTTPMiddleware):

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

        if "authorization" in request.headers and "Bearer" in request.headers["authorization"]:
            token = request.headers["authorization"].split(" ")[-1]
            try:
                user = jwt.decode(token, SECRET_KEY, ALGORITHM)
            except Exception:
                return JSONResponse(status_code=401, content={"success": False, "token": False, "message": "Signature has expired"})

            request.state.user = user["id"]
            return await call_next(request)
        else:
            return JSONResponse(status_code=401, content={"success": False, "message": "Authorization header not found"})
