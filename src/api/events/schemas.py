from pydantic import BaseModel
from typing import List, Optional

class EventSchema(BaseModel):
    event_id: int
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventListSchema(BaseModel):
    results: List[EventSchema]

class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str] = ""

class EventUpdateSchema(BaseModel):
    description: str