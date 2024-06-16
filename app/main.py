from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, users, account

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(account.router)