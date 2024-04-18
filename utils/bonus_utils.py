MAX_ACC_BONUS = 1000
MAX_WALLET_BONUS = 500

SAME_BANK_BONUS = 20
WALLET_BONUS = 10

TRANSFER_AMOUNT_BONUS_0_100 = 10
TRANSFER_AMOUNT_BONUS_101_500 = 20
TRANSFER_AMOUNT_BONUS_501_ = 30

ACCOUNT_AGE_BONUS_0_5 = 30
ACCOUNT_AGE_BONUS_6_10 = 20
ACCOUNT_AGE_BONUS_11_ = 10

def get_max_acc_bonus(month):
    bonus = {
        "jan": MAX_ACC_BONUS,
        "feb": MAX_ACC_BONUS // 2
    }
    return bonus[month]

def get_max_wallet_bonus(month):
    bonus = {
        "jan": MAX_WALLET_BONUS,
        "feb": MAX_WALLET_BONUS // 2
    }
    return bonus[month]

def get_same_bank_bonus(month):
    bonus = {
        "jan": SAME_BANK_BONUS,
        "feb": SAME_BANK_BONUS // 2
    }
    return bonus[month]

def get_wallet_bonus(month):
    bonus = {
        "jan": WALLET_BONUS,
        "feb": WALLET_BONUS // 2
    }
    return bonus[month]

def get_transfer_amount_bonus(amount):
    if amount <= 100:
        return TRANSFER_AMOUNT_BONUS_0_100
    elif amount <= 500:
        return TRANSFER_AMOUNT_BONUS_101_500
    else:
        return TRANSFER_AMOUNT_BONUS_501_

def get_account_age_bonus(age):
    if age <= 5:
        return ACCOUNT_AGE_BONUS_0_5
    elif age <= 10:
        return ACCOUNT_AGE_BONUS_6_10
    else:
        return ACCOUNT_AGE_BONUS_11_