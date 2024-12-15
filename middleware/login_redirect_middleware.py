from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from services.user_service import UserService

class LoginRedirectMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Exclude paths that don't require authentication
        excluded_paths = ["/auth/login", "/auth/register"]
        
        # Check if the path is excluded; if so, redirect to dashboard as the user is already logged in
        if request.url.path in excluded_paths:
            # Check if the user is logged in
            if UserService.is_loggedin():
                # Redirect to login page if not logged in
                return RedirectResponse(
                    url="/auth/dashboard",
                    status_code=303
                )
        
        # Process the request otherwise
        response = await call_next(request)
        return response