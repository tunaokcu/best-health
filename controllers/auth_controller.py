from fastapi import APIRouter, HTTPException, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.auth_service import AuthService
from starlette.responses import HTMLResponse

router = APIRouter()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the login page
@router.get("/login")
async def get_login_page(request: Request, error: str = None, message: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "error": error, "message": message})

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if not AuthService.login(username, password):
        # Redirect to the login page with an error message
        return RedirectResponse(url="/auth/login?error=Invalid credentials", status_code=303)
    
    # Redirect to a dummy page with a logout button
    return RedirectResponse(url="/auth/dummy", status_code=303)

# Render the dummy page
@router.get("/dummy", response_class=HTMLResponse)
async def dummy_page(request: Request):
    return templates.TemplateResponse("dummy.html", {"request": request})

# Logout function (optional)
@router.get("/logout")
async def logout():
    return RedirectResponse(url="/auth/login", status_code=303)

@router.post("/signup")
async def signup(username: str = Form(...), password: str = Form(...)):
    created_user = AuthService.signup(username, password)
    if not created_user:
        # Redirect to the login page with an error message
        return RedirectResponse(url="/auth/login?error=Username already taken", status_code=303)
    
    # Redirect to the login page with a success message
    return RedirectResponse(url="/auth/login?message=Registered successfully", status_code=303)

"""
@router.post("/logout")
async def logout():
    # In a real scenario, this would handle session/token invalidation
    if not AuthService.logout():
        raise HTTPException(status_code=400, detail="Logout failed")
    return {"message": "Logged out successfully"}

"""
