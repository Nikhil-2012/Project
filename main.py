import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, users, account

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(account.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)