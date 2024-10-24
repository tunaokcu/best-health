from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from controllers import auth_controller

app = FastAPI()

# Serve static files (e.g., CSS/JS)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the router from the auth controller
app.include_router(auth_controller.router, prefix="/auth")

