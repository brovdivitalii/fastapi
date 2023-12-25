from fastapi import FastAPI
from database import database, engine
from models import metadata, notes  # Додайте імпорт таблиці з models
from crud import get_notes, create_note, update_note, delete_note

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

@app.get("/notes")
async def read_notes():
    return await get_notes(database)

@app.post("/notes")
async def create_note_api(note: str):
    return await create_note(database, note)

@app.put("/notes/{note_id}")
async def update_note_api(note_id: int, new_note: str):
    return await update_note(database, note_id, new_note)

@app.delete("/notes/{note_id}")
async def delete_note_api(note_id: int):
    return await delete_note(database, note_id)
