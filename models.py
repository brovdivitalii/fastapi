from sqlalchemy import Column, Integer, String, MetaData, Table

metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("content", String),
)
