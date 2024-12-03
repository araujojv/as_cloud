from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    id: str = Field(None, alias="_id")
    nome:str
    email: EmailStr