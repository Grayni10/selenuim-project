import pytest
from bank_account import BankAccount

@pytest.fixture
def bank_account():
    return BankAccount(account_number="123456", balance=100)

def test_deposit_functionality(bank_account):
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150

def test_deposit_negative_amount(bank_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        bank_account.deposit(-50)

def test_withdraw_functionality(bank_account):
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdrawal_exceeding_balance(bank_account):
    with pytest.raises(ValueError, match="Insufficient funds."):
        bank_account.withdraw(150)

def test_get_balance_method(bank_account):
    assert bank_account.get_balance() == 100

def test_withdraw_with_negative_amount(bank_account):
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        bank_account.withdraw(-30)
