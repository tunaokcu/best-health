from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from controllers import auth_controller

app = FastAPI()
app.include_router(auth_controller.router, prefix="/auth")