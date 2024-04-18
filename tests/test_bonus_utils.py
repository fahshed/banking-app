from utils import bonus_utils


def test_get_max_acc_bonus():
    assert bonus_utils.get_max_acc_bonus("jan") == 1000
    assert bonus_utils.get_max_acc_bonus("feb") == 500

def test_get_max_wallet_bonus():
    assert bonus_utils.get_max_wallet_bonus("jan") == 500
    assert bonus_utils.get_max_wallet_bonus("feb") == 250

def test_get_same_bank_bonus():
    assert bonus_utils.get_same_bank_bonus("jan") == 20
    assert bonus_utils.get_same_bank_bonus("feb") == 10

def test_get_wallet_bonus():
    assert bonus_utils.get_wallet_bonus("jan") == 10
    assert bonus_utils.get_wallet_bonus("feb") == 5

def test_get_transfer_amount_bonus():
    assert bonus_utils.get_transfer_amount_bonus(50) == 10  # For amount <= 100
    assert bonus_utils.get_transfer_amount_bonus(300) == 20  # For amount <= 500
    assert bonus_utils.get_transfer_amount_bonus(600) == 30  # For amount > 500

def test_get_account_age_bonus():
    assert bonus_utils.get_account_age_bonus(3) == 30  # For age <= 5
    assert bonus_utils.get_account_age_bonus(8) == 20  # For age <= 10
    assert bonus_utils.get_account_age_bonus(15) == 10  # For age > 10