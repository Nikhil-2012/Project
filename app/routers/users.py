from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, security
from ..models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/me", response_model=schemas.UserResponse)
def read_users_me(current_user: User = Depends(security.get_current_user)):
    return current_user

@router.put("/me/", response_model=schemas.UserResponse)
def update_user_me(user_update: schemas.UserCreate, current_user: User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    current_user.hashed_password = crud.get_password_hash(user_update.password)
    current_user.email = user_update.email
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user

@router.delete("/me/", response_model=schemas.UserResponse)
def delete_user_me(current_user: User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    db.delete(current_user)
    db.commit()
    return current_user

