import pytest
from utils.transfer_utils import get_transfer_bonus

@pytest.mark.parametrize(
    "transfer_amount, is_to_wallet, same_bank_transfer, recipient_account_age, expected_bonus",
    [
        # Weak normal equivalence class test cases
        (30, True, True, 3, 30), 
        (200, False, True, 8, 50),
        (600, False, False, 15, 40),  

        # Boundary value test cases
        (-1, False, False, 0, -1), 
        (0, False, False, -1, -1),  
        (100, True, True, 5, 30),  
        (101, True, True, 6, 40),  
        (500, False, True, 10, 50),
        (501, False, True, 11, 60),  
    ]
)

def test_get_transfer_bonus(transfer_amount, is_to_wallet, same_bank_transfer, recipient_account_age, expected_bonus):
    bonus = get_transfer_bonus(transfer_amount, is_to_wallet, same_bank_transfer, recipient_account_age)
    assert bonus == expected_bonus