from pydantic import BaseModel
from datetime import datetime as date


class Note(BaseModel):
    id: str
    note: str
    important : bool = False
    created_at: str = "Not specified"
    updated_at: str = "Not specified" 
    def __init__(self, **data):
        super().__init__(**data)
        self.created_at = self.created_at or date.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.updated_at or date.now().strftime("%Y-%m-%d %H:%M:%S")