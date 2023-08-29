from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class Roles(Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[int]
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: Optional[bool] = True
    role: Optional[Roles] = Roles.user