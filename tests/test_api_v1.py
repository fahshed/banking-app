from dotenv import dotenv_values
from fastapi.testclient import TestClient
from pymongo import MongoClient

from main import app
from database import get_prod_collection
from tests.database import get_test_collection


config = dotenv_values(".env")

app.dependency_overrides[get_prod_collection] = get_test_collection


class TestAccount:
    client = TestClient(app)
    mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    database = mongodb_client["test-db"]
    collection = database["accounts"]


    def test_create_account(self):
        account_data = {
            "accountNumber": 0,
            "firstName": "string",
            "lastName": "string",
            "accountBalance": 0,
            "walletBalance": 0,
            "accountAge": 0
        }
        
        response = self.client.post("/account/", json=account_data)

        assert response.status_code == 201
        created_account = response.json()
        assert created_account["accountNumber"] == account_data["accountNumber"]
        assert created_account["lastName"] == account_data["lastName"]

        self.collection.drop()


    def test_show_accounts(self):
        response = self.client.get("/account/all/")
        
        assert response.status_code == 200
        accounts = response.json()

        assert isinstance(accounts, list)

        self.collection.drop()


    def test_deposit_into_account(self):
        account_data = {
            "accountNumber": 1234,
            "firstName": "string",
            "lastName": "string",
            "accountBalance": 1000,
            "walletBalance": 0,
            "accountAge": 0
        }
        response = self.client.post("/account/", json=account_data)
        assert response.status_code == 201

        deposit_data = {
            "accountNumber": account_data["accountNumber"],
            "amount": 1000
        }
        response = self.client.post("/account/deposit/", json=deposit_data)
        
        assert response.status_code == 200
        assert response.json() == {"message": "Deposit successful"}

        self.collection.drop()


    def test_withdraw_from_account(self):
        account_data = {
            "accountNumber": 123,
            "firstName": "string",
            "lastName": "string",
            "accountBalance": 1000,
            "walletBalance": 0,
            "accountAge": 0
        }
        response = self.client.post("/account/", json=account_data)
        assert response.status_code == 201

        withdrawal_data = {
            "accountNumber": 123,
            "amount": 500
        }
        response = self.client.post("/account/withdraw/", json=withdrawal_data)
        
        assert response.status_code == 200
        assert response.json() == {"message": "Withdraw successful"}

        self.collection.drop()