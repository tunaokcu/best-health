from fastapi import APIRouter, HTTPException, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.user import User
from services.auth_service import AuthService
from starlette.responses import HTMLResponse

router = APIRouter()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the login page
@router.get("/login")
async def get_login_page(request: Request, error: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "error": error})

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
async def signup(user: User):
    created_user = AuthService.signup(user)
    if not created_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    return {"message": "User created successfully"}

@router.post("/logout")
async def logout():
    # In a real scenario, this would handle session/token invalidation
    if not AuthService.logout():
        raise HTTPException(status_code=400, detail="Logout failed")
    return {"message": "Logged out successfully"}

