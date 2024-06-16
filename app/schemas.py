from pydantic import BaseModel, Field, EmailStr, constr
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    username: constr(strip_whitespace=True, min_length=1)
    email: EmailStr
    password: constr(strip_whitespace=True, min_length=1)

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    timestamp: datetime
    description: Optional[str]

    class Config:
        orm_mode = True
