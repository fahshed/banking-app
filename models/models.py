from typing import Optional
from pydantic import BaseModel

class AccountModel(BaseModel):
    accountNumber: int
    firstName: str
    lastName: str
    accountBalance: int
    walletBalance: int
    accountAge: int

class DepositWithDrawModel(BaseModel):
    accountNumber: int
    amount: int

class TransferModel(BaseModel):
    isToWallet: bool
    fromAccountNumber: int
    toAccountNumber: Optional[int]
    amount: int
