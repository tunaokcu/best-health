from fastapi import APIRouter, HTTPException, Form, Request
from fastapi.templating import Jinja2Templates
from models.user import User
from services.auth_service import AuthService

router = APIRouter()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the login page
@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if not AuthService.login(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Logged in successfully"}


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

