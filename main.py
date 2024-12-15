from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import Request
from controllers import auth_controller
from controllers import room_controller
from controllers import patient_controller
from controllers import admission_controller


app = FastAPI(debug=True)

# Serve static files(CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_controller.router, prefix="/auth")
app.include_router(room_controller.router, prefix="/rooms")
app.include_router(patient_controller.router, prefix="/patients")
app.include_router(admission_controller.router, prefix="/admissions")

"""
# Redirect all requests to the root ("/") to "/auth/login"
@app.get("/")
async def root_redirect():
    return RedirectResponse(url="/auth/login")

# Redirect all requests to ("/auth") to "/auth/login"
@app.get("/auth")
async def auth_redirect():
    return RedirectResponse(url="/auth/login")"""