from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.user_service import UserService
from starlette.responses import HTMLResponse

router = APIRouter()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the register page
@router.get("/register")
async def get_register_page(request: Request, error: str = None, message: str = None):
    return templates.TemplateResponse("register.html", {"request": request, "error": error, "message": message})

# Render the login page
@router.get("/login")
async def get_login_page(request: Request, error: str = None, message: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "error": error, "message": message})

# Handle form submissions to login
@router.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    if not UserService.login(email, password):
        # Redirect to the login page with an error message
        return RedirectResponse(url="/auth/login?error=Invalid credentials", status_code=303)
    
    # Redirect to the dashboard with a logout button
    return RedirectResponse(url="/auth/dashboard", status_code=303)

# Render the dummy dashboard page
@router.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard_page(request: Request, permission: bool = Depends(UserService.is_loggedin)):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Redirect from dashboard(dummy) to login
@router.get("/logout")
async def logout():
    UserService.logout()
    return RedirectResponse(url="/auth/login", status_code=303)

@router.post("/register")
async def register(firstname: str = Form(...), lastname: str = Form(...), email: str = Form(...), password: str = Form(...)):
    created_user = UserService.signup(firstname, lastname, email, password)
    if not created_user:
        # Redirect to the login page with an error message
        return RedirectResponse(url="/auth/register?error=Email in use", status_code=303)
    
    # Redirect to the login page with a success message
    return RedirectResponse(url="/auth/login?message=Registered successfully", status_code=303)