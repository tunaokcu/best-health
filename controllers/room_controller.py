from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.room_service import RoomService
from starlette.responses import HTMLResponse



router = APIRouter()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Render the create room page
@router.get("/create")
async def get_create_room_page(request: Request, error: str = None, message: str = None):
    return templates.TemplateResponse("create_room.html", {"request": request, "error": error, "message": message})

# Handle form submission to create a room
@router.post("/create")
async def create_room(name: str = Form(...), status: str = Form(...), type: str = Form(...), description: str = Form(...)):
    result = await RoomService.create_room(name, status, type, description)
    if not result:
        # Redirect to the create room page with an error message
        return RedirectResponse(url="/rooms/create?error=Failed to create room", status_code=303)
    
    # Redirect to the room list page with a success message
    return RedirectResponse(url="/rooms?message=Room created successfully", status_code=303)

# Render the room list page
@router.get("/", response_class=HTMLResponse)
async def get_rooms_page(request: Request, message: str = None):
    rooms = await RoomService.get_all_rooms()
    print(rooms)
    return templates.TemplateResponse("rooms.html", {"request": request, "rooms": rooms, "message": message})

# Render the room details page
@router.get("/{id}", response_class=HTMLResponse)
async def get_room_details_page(request: Request, id: int):
    room = await RoomService.get_room_by_id(id)
    if not room:
        return RedirectResponse(url="/rooms?error=Room not found", status_code=303)
    return templates.TemplateResponse("room_details.html", {"request": request, "room": room})
