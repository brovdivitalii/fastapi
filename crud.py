from sqlalchemy.sql import select
from models import notes  # Додайте імпорт таблиці з models

async def get_notes(database):
    query = select(notes)
    return await database.fetch_all(query)

async def create_note(database, note: str):
    query = notes.insert().values(content=note)
    return await database.execute(query)

async def update_note(database, note_id: int, new_note: str):
    query = notes.update().where(notes.c.id == note_id).values(content=new_note)
    return await database.execute(query)

async def delete_note(database, note_id: int):
    query = notes.delete().where(notes.c.id == note_id)
    return await database.execute(query)
