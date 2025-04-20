from fastapi import FastAPI
from routes.user import user 
from routes.auth import auth_routers
from routes.task import task
import models
from config.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(auth_routers)
app.include_router(user)
app.include_router(task)
