from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, crud, database, security

router = APIRouter(
    prefix="/account",
    tags=["account"],
)


@router.post("/add", response_model=schemas.TransactionResponse)
def add_money(
        transaction: schemas.TransactionCreate,
        current_user: models.User = Depends(security.get_current_user),
        db: Session = Depends(database.get_db)
):
    if transaction.amount <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Amount must be greater than zero")

    crud.update_user_balance(db, current_user, transaction.amount)
    new_transaction = crud.create_transaction(db, current_user.id, transaction.amount, transaction.description)
    return new_transaction


@router.post("/remove", response_model=schemas.TransactionResponse)
def remove_money(
        transaction: schemas.TransactionCreate,
        current_user: models.User = Depends(security.get_current_user),
        db: Session = Depends(database.get_db)
):
    if transaction.amount <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Amount must be greater than zero")
    if transaction.amount > current_user.balance:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient balance")

    crud.update_user_balance(db, current_user, -transaction.amount)
    new_transaction = crud.create_transaction(db, current_user.id, -transaction.amount, transaction.description)
    return new_transaction


@router.get("/balance", response_model=float)
def get_balance(current_user: models.User = Depends(security.get_current_user)):
    return current_user.balance


@router.get("/history", response_model=list[schemas.TransactionResponse])
def get_transaction_history(
        current_user: models.User = Depends(security.get_current_user),
        db: Session = Depends(database.get_db)
):
    transactions = db.query(models.Account).filter(models.Account.user_id == current_user.id).all()
    return transactions

