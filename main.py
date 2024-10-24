from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from controllers import auth_controller

app = FastAPI()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="/templates")

# Serve static files (e.g., CSS/JS)
app.mount("/static", StaticFiles(directory="/static"), name="static")

# Include the router from the auth controller
app.include_router(auth_controller.router, prefix="/auth")

# Render the login page
@app.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})