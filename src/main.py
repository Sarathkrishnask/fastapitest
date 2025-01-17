from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import smoketest

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(smoketest.router, prefix="/smoke-test")

# Define the API endpoints
@app.get('/')
def health():
    return {
        "message": "OK 🚀"
    }
