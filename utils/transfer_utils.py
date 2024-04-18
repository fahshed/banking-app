'''
Transfer rules: Receiving account bonus (Depends on the current month)

Following are for the month of January:
1. To Same Bank Acc Bonus -> 20$
2. To Wallet Bonus -> 10$
3. Transfer Amount Bonus -> 
    0-100: 10$, 
    101-500: 20$, 
    500+: 30$, 
4. Account age -> 
    0-5: 30$, 
    6-10: 20$, 
    10+: 10$ 

Maximum account transfer bonus will be 1000 USD
Maximum wallet transfer bonus will be 500 USD
'''


from .bonus_utils import get_account_age_bonus, get_max_acc_bonus, get_max_wallet_bonus, get_same_bank_bonus, get_transfer_amount_bonus, get_wallet_bonus


def get_transfer_bonus(
    transfer_amount, 
    is_to_wallet, 
    same_bank_transfer, 
    recipient_account_age
):
    if transfer_amount < 0 or recipient_account_age < 0:
        return -1
    
    month = "jan"
    
    transfer_amount_bonus = 0

    if is_to_wallet:
        transfer_amount_bonus += get_wallet_bonus(month)
    elif same_bank_transfer:
        transfer_amount_bonus += get_same_bank_bonus(month)

    transfer_amount_bonus += get_transfer_amount_bonus(transfer_amount)

    transfer_amount_bonus += get_account_age_bonus(transfer_amount)

    if is_to_wallet:
        return min(transfer_amount_bonus, get_max_wallet_bonus(month))
    
    return min(transfer_amount_bonus, get_max_acc_bonus(month))
