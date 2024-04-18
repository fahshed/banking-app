from typing import List
from pymongo.collection import Collection
from fastapi import APIRouter, Depends, HTTPException, status

from database import get_prod_collection
from models.models import AccountModel, DepositWithDrawModel, TransferModel
from utils.transfer_utils import get_transfer_bonus


router = APIRouter()


@router.post("/", response_description='create an account', status_code=status.HTTP_201_CREATED, response_model=AccountModel)
def create_account(account: AccountModel, collection: Collection = Depends(get_prod_collection)):
    new_account = collection.insert_one(dict(account))
    created_account = collection.find_one({
        "_id": new_account.inserted_id
    })
    return created_account


@router.get("/all", response_description="list all the accounts", response_model=List[AccountModel])
def show_accounts(collection: Collection = Depends(get_prod_collection)):
    accounts = list(collection.find())
    return accounts


@router.post("/deposit", response_description='deposit money into an account', status_code=status.HTTP_200_OK)
def deposit_into_account(deposit: DepositWithDrawModel, collection: Collection = Depends(get_prod_collection)):
    deposit = dict(deposit)
    accountNumber = deposit["accountNumber"]
    amount = deposit["amount"]
    updated = collection.update_one({"accountNumber": accountNumber}, {"$inc": {"accountBalance": amount} })
    if updated.modified_count == 1:
        return {"message": "Deposit successful"}
    raise HTTPException(status_code=404, detail="Account not found or deposit failed")


@router.post("/withdraw", response_description='withdraw money from an account', status_code=status.HTTP_200_OK)
def withdraw_from_account(withdraw: DepositWithDrawModel, collection: Collection = Depends(get_prod_collection)):
    withdraw = dict(withdraw)
    accountNumber = withdraw["accountNumber"]
    amount = withdraw["amount"]
    updated = collection.update_one({"accountNumber": accountNumber}, {"$inc": {"accountBalance": -1 * amount} })
    if updated.modified_count == 1:
        return {"message": "Withdraw successful"}
    raise HTTPException(status_code=404, detail="Account not found or Withdraw failed")


@router.post("/transfer", response_description='transfer money from an account', status_code=status.HTTP_200_OK)
def transfer(transfer: TransferModel, collection: Collection = Depends(get_prod_collection)):
    transfer = dict(transfer)
    is_to_wallet = transfer["isToWallet"]
    from_account_number =  transfer["fromAccountNumber"]
    to_account_number = transfer["toAccountNumber"]
    amount = transfer["amount"]

    if is_to_wallet:
        receiving_account_number = from_account_number
        receiving_update_field = "walletBalance"
    else:
        receiving_account_number = to_account_number
        receiving_update_field = "accountBalance"

    receiving_account = collection.find_one({
        "accountNumber": receiving_account_number
    })

    transfer_bonus = get_transfer_bonus(amount, is_to_wallet, receiving_account != None, receiving_account["accountAge"])
    transfer_amount = amount + transfer_bonus

    updated1 = collection.update_one({"accountNumber": from_account_number}, {"$inc": {"accountBalance": -1 * amount} })
    updated2 = collection.update_one({"accountNumber": receiving_account_number}, {"$inc": {receiving_update_field: transfer_amount} })

    if updated1.modified_count + updated2.modified_count == 2:
        return {"message": "Transfer successful"}
    raise HTTPException(status_code=404, detail="Account not found or transfer failed")