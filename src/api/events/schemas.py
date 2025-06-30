from pydantic import BaseModel

class EventSchema(BaseModel):
    event_id: int