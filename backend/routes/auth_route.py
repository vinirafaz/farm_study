from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User


auth = APIRouter(prefix="/auth")


@auth.post("/login")
async def login(user: User):
    username = dict(user)["email"]
    password = dict(user)["password"]

    if True:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")