from pydantic import BaseModel

class MonSchema(BaseModel):
    nom: str
    description: str
