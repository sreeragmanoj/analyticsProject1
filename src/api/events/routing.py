from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema
router = APIRouter()


# get method for listing the events
@router.get('/')
def read_events() -> EventSchema:
    return {
        "results": [{'event_id': 1}, {'event_id': 2}, {'event_id': 3}]
    }

# post method for creating an event
@router.post('/')
def create_event(payload: EventCreateSchema) -> EventSchema:
    data = payload.model_dump()
    return { "event_id": 1, **data}
#
# get method for reading a specific event by its ID
@router.get("/{event_id}")
def read_event(event_id: int) -> EventSchema:
    return {
        "event_id": event_id,
    }

# Put method for updating an event
@router.put("/{event_id}")
def read_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    data = payload.model_dump()
    return {
        "event_id": event_id,
        **data
    }

