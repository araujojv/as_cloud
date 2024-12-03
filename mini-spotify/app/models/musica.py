from pydantic import BaseModel, Field

class Musica(BaseModel):
    id: str = Field(None, alias="_id")
    titulo: str

