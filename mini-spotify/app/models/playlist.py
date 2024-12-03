from pydantic import BaseModel, Field
from typing import List

class Playlist(BaseModel):
    id: str = Field(None, alias="_id")
    nome: str
    usuario_id: str
    musicas: List[str] = []
