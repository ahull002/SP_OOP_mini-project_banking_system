from random import randint

class Client:

    # {account_number: xxxxx, name: "xxxxxx", balance: xxxx}
    account = {}

    def __init__(self, name, address, account, deposit):
        self.account['account_number'] = randint(10000, 99999)
        self.account['name'] = name
        self.account['address'] = address
        self.account['account type'] = account
        self.account['balance'] = deposit

    def withdraw(self, amount):
        if self.account['balance'] >= amount:
            self.account['balance'] -= amount
            print()
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
            self.balance()
        else:
            print()
            print("Insufficient funds!")
            self.balance()

    def deposit(self, amount):
        self.account['balance'] += amount
        print()
        print("The sum of {} has been added to your account balance.".format(amount))
        self.balance()

    def balance(self):
        print()
        print("Your current account balance is: {} ".format(self.account['balance']))