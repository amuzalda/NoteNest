from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from datetime import datetime as date



templates = Jinja2Templates(directory="templates")
note = APIRouter()
# note.mount("/static", StaticFiles(directory="static"), name="static")
@note.get("/", response_model=list[Note])
async def get_notes(request: Request):
    """
    Retrieve all notes.
    """
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        id = doc.get("_id")
        note = doc.get("note")
        important = doc.get("important", False)
        created_at = doc.get("created_at", "Not specified")
        updated_at = doc.get("updated_at", "Not specified")
        
        newDocs.append({
            "id": str(id),
            "note": note,
            "important": important,
            "created_at": created_at,
            "updated_at": updated_at
        })
    return templates.TemplateResponse("index.html", {"request": request, "notes": newDocs})

@note.get("/notes/{id}", response_model=Note)
async def get_note(request: Request, id: str):  
    """
    Retrieve a note by its ID.
    """
    doc = conn.notes.notes.find_one({"_id": id})
    if doc:
        return noteEntity(doc)
    return {"error": "Note not found"}  

@note.post("/", response_model=Note)
async def create_note(request: Request, note: Note):  
    """
    Create a new note.
    """
    print(request, note)
    new_note = {
        "note": "new note",
        "important": "false",
        "created_at": str(date.now()),
        "updated_at": str(date.now())
    }
    result = conn.notes.notes.insert_one(new_note)
    new_note["_id"] = result.inserted_id
    return noteEntity(new_note)
