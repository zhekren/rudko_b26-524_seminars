class BankError(Exception):
    pass

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountBlockedError(BankError):
    pass

balance = 10000
amount = int(input("Введите сумму для снятия: "))

def withdraw(balance, amount):
    result_balance  = balance - amount
    if amount <= 0:
        raise InvalidAmountError("Сумма равна нулю или меньше")
    if amount > balance:
        raise InsufficientFundsError("Недостаточно средств")
    return result_balance

try:
    print(withdraw(balance, amount))
except BankError as e:
    print(e)
