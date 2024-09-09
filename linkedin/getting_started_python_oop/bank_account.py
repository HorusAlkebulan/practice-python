# bank_account.py


class BankAccount:
    def __init__(self, account_number, account_holder, account_balance: float = 0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._account_balance = account_balance

    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder

    def get_account_balance(self):
        return self._account_balance

    def set_account_number(self, number):
        self._account_number = number

    def set_balance(self, balance: float):
        if balance >= 0.0:
            self._account_balance == balance
        else:
            raise ValueError(f"Cannot set negative balance: {balance}")


if __name__ == "__main__":

    account = BankAccount(
        account_number="987654",
        account_holder="Horus Alkebu-Lan",
        account_balance=10000.00,
    )
    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Account Balance: {account.get_account_balance()}")

    new_balance = -1.0
    try:
        account.set_balance(new_balance)
    except ValueError as e:
        print(e)

    new_balance = 10500.000
    account.set_balance(new_balance)

    print(f"New balance is {account.get_account_balance()}")
