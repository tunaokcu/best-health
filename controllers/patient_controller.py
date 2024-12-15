from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.patient_service import PatientService
from services.user_service import UserService
from starlette.responses import HTMLResponse
from typing import Optional

import logging

logger = logging.getLogger("uvicorn")

router = APIRouter(dependencies=[Depends(UserService.is_loggedin)])

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the register patient page
@router.get("/register")
async def get_register_patient_page(request: Request, error: str = None, message: str = None):
    logger.debug("Register route accessed")
    return templates.TemplateResponse("register_patient.html", {"request": request, "error": error, "message": message})

# Handle form submission to register a new patient
@router.post("/register")
async def register_patient(firstname: str = Form(...), lastname: str= Form(...), gender: str =Form(...), date_of_birth: str = Form(...), address: str = Form(...), contact: str = Form(...),     medical_history: Optional[str] = Form(None),):
    logger.debug("Register route accessed")
    result = PatientService.register_patient(firstname, lastname, gender, date_of_birth, address, contact, medical_history)
    if not result:
        # Redirect to the patient registration page with an error message
        return RedirectResponse(url="/patients/register?error=Patient registration failed", status_code=303)
    
    # Redirect to the patient list page with a success message
    return RedirectResponse(url="/patients?message=Patient registered successfully", status_code=303)

# Render the patient list page
@router.get("/", response_class=HTMLResponse)
async def get_patients_page(request: Request, message: str = None):
    patients = PatientService.get_all_patients()
    return templates.TemplateResponse("patient_list.html", {"request": request, "patients": patients, "message": message})

# Render patient details page
@router.get("/{id}", response_class=HTMLResponse)
async def get_patient_details_page(request: Request, id: int):
    patient = PatientService.get_patient(id)
    if not patient:
        return RedirectResponse(url="/patients?error=Patient not found", status_code=303)
    return templates.TemplateResponse("patient_details.html", {"request": request, "patient": patient})
