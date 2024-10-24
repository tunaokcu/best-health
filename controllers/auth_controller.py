from fastapi import APIRouter, HTTPException, Depends
from models.user import User
from services.auth_service import AuthService

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    created_user = AuthService.signup(user)
    if not created_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    return {"message": "User created successfully"}

@router.post("/login")
async def login(user: User):
    if not AuthService.login(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Logged in successfully"}

@router.post("/logout")
async def logout():
    # In a real scenario, this would handle session/token invalidation
    if not AuthService.logout():
        raise HTTPException(status_code=400, detail="Logout failed")
    return {"message": "Logged out successfully"}
