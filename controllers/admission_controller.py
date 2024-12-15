from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.admission_service import AdmissionService
from services.user_service import UserService
from starlette.responses import HTMLResponse

router = APIRouter(dependencies=[Depends(UserService.is_loggedin)])

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the admit patient page
@router.get("/admit")
def get_admit_patient_page(request: Request, error: str = None, message: str = None):
    return templates.TemplateResponse("admit_patient.html", {"request": request, "error": error, "message": message})

# Handle form submission to admit a patient
@router.post("/admit")
def admit_patient(patient_id: int = Form(...), room_id: int = Form(...), admission_date: str = Form(...), reason: str = Form(...)):
    result = AdmissionService.admit_patient(patient_id, room_id, admission_date, reason)
    if not result:
        # Redirect to the admit patient page with an error message
        return RedirectResponse(url="/admissions/admit?error=Admission failed", status_code=303)
    
    # Redirect to the admission list page with a success message
    return RedirectResponse(url="/admissions?message=Patient admitted successfully", status_code=303)

# Render the admission list page
@router.get("/", response_class=HTMLResponse)
def get_admissions_page(request: Request, message: str = None):
    admissions = AdmissionService.get_all_admissions()
    return templates.TemplateResponse("admission_list.html", {"request": request, "admissions": admissions, "message": message})

# Render admission details page
@router.get("/{id}", response_class=HTMLResponse)
def get_admission_details_page(request: Request, id: int):
    admission = AdmissionService.get_admission_details(id)
    if not admission:
        return RedirectResponse(url="/admissions?error=Admission not found", status_code=303)
    return templates.TemplateResponse("admission_details.html", {"request": request, "admission": admission})
