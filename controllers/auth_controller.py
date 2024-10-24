from fastapi import APIRouter, HTTPException, Form
from models.user import User
from services.auth_service import AuthService

router = APIRouter()


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
