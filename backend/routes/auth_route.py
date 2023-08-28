from fastapi import APIRouter, Depends, HTTPException, status

auth = APIRouter(prefix="/auth")


@auth.post("/login")
async def login():
    return {"message": "Login!"}