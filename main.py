from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import Request
from controllers import auth_controller

app = FastAPI()
app.include_router(auth_controller.router, prefix="/auth")


# Redirect all requests to the root ("/") to "/auth/login"
@app.get("/")
async def root_redirect():
    return RedirectResponse(url="/auth/login")

# Redirect all requests to ("/auth") to "/auth/login"
@app.get("/auth")
async def auth_redirect():
    return RedirectResponse(url="/auth/login")