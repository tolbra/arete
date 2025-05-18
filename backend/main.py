from fastapi import FastAPI
from routes.daily import router as daily_router
from routes.daily import router as daily_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(daily_router, prefix="/daily")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
