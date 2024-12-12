from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.patient_service import PatientService
from starlette.responses import HTMLResponse

router = APIRouter()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the register patient page
@router.get("/register")
async def get_register_patient_page(request: Request, error: str = None, message: str = None):
    return templates.TemplateResponse("register_patient.html", {"request": request, "error": error, "message": message})

# Handle form submission to register a new patient
@router.post("/register")
async def register_patient(name: str = Form(...), date_of_birth: str = Form(...), address: str = Form(...), contact: str = Form(...), medical_history: str = Form(...)):
    result = await PatientService.register_patient(name, date_of_birth, address, contact, medical_history)
    if not result:
        # Redirect to the patient registration page with an error message
        return RedirectResponse(url="/patients/register?error=Patient registration failed", status_code=303)
    
    # Redirect to the patient list page with a success message
    return RedirectResponse(url="/patients?message=Patient registered successfully", status_code=303)

# Render the patient list page
@router.get("/", response_class=HTMLResponse)
async def get_patients_page(request: Request, message: str = None):
    patients = await PatientService.get_all_patients()
    return templates.TemplateResponse("patient_list.html", {"request": request, "patients": patients, "message": message})

# Render patient details page
@router.get("/{id}", response_class=HTMLResponse)
async def get_patient_details_page(request: Request, id: int):
    patient = await PatientService.get_patient(id)
    if not patient:
        return RedirectResponse(url="/patients?error=Patient not found", status_code=303)
    return templates.TemplateResponse("patient_details.html", {"request": request, "patient": patient})
