from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()

def create_transaction(db: Session, user_id: int, amount: float, description: Optional[str] = None) -> models.Account:
    account = models.Account(user_id=user_id, amount=amount, description=description)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def update_user_balance(db: Session, user: models.User, amount: float) -> models.User:
    user.balance += amount
    db.commit()
    db.refresh(user)
    return user

