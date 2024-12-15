from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from services.user_service import UserService

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Exclude paths that don't require authentication
        excluded_paths = ["/auth/login", "/auth/register"]
        
        # Check if the path is excluded
        if request.url.path not in excluded_paths:
            # Check if the user is logged in
            if not UserService.is_loggedin():
                # Redirect to login page if not logged in
                return RedirectResponse(
                    url="/auth/login?error=You must log in to see this page",
                    status_code=303
                )
        
        # Process the request if authenticated or excluded
        response = await call_next(request)
        return response
