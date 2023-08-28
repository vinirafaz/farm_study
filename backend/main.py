from fastapi import FastApi
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import routes

app = FastApi()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)



@app.get("/")
async def index():
    return {"message": "Welcome to the API"}

app.include_router(routes.router)