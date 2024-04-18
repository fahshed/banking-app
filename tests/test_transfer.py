from dotenv import dotenv_values
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from fastapi.testclient import TestClient
from pymongo import MongoClient

from database import get_prod_collection
from main import app
from tests.database import get_test_collection


config = dotenv_values(".env")

app.dependency_overrides[get_prod_collection] = get_test_collection

client = TestClient(app)

@scenario("transfer.feature", "Transfer money from one account to another")
def test_transfer():
    pass

@pytest.fixture
def step_context():
    return {'response': None}

@given(parsers.parse("there is an account with account number {account_number:d} and balance {balance:d}"))
def setup_mock_account1(account_number, balance):
    account_data = {
        "accountNumber": int(account_number),
        "firstName": "string",
        "lastName": "string",
        "accountBalance": int(balance),
        "walletBalance": 0,
        "accountAge": 0
    }
    client.post("/account/", json=account_data)


@when(parsers.parse("I transfer {amount:d} from account {from_account_number:d} to account {to_account_number:d}"))
def transfer_money(amount, from_account_number, to_account_number, step_context):
    transfer_data = {
        "isToWallet": False,
        "fromAccountNumber": int(from_account_number),
        "toAccountNumber": int(to_account_number),
        "amount": int(amount)
    }
    response = client.post("/account/transfer", json=transfer_data)
    step_context['response'] = response 

@then("the transfer should be successful")
def check_transfer_success(step_context):
    transfer_response = step_context['response']
    assert transfer_response.status_code == 200
    assert transfer_response.json() == {"message": "Transfer successful"}

    mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    database = mongodb_client["test-db"]
    collection = database["accounts"]
    collection.drop()