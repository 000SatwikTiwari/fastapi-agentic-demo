from fastapi import FastAPI
from app.models import Note
from app.storage import notes_db

app = FastAPI()

@app.post("/notes")
def create_note(note: Note):
    notes_db.append(note.dict())
    return {"message": "Note created"}

@app.get("/notes")
def list_notes():
    return notes_db

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    return notes_db[note_id]