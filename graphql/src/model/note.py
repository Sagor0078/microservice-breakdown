from typing import Optional
from sqlmodel import SQLModel, Field 

class Note(SQLModel, table=True):
    __tablename__ = "note"

    id: Optional[int] = Field(None,primary_key=True,nullable=True)
    name:str
    description:str
