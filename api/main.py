from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import login

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
