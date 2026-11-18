from fastapi import FastAPI
from server.routes import user

app = FastAPI()

app.include_router(user.router)