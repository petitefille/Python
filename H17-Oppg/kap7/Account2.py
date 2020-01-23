class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions +=1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions +=1

    def dump(self):
        s = '%s, %s, balance: %s, transactions: %s' % \
            (self.name, self.no, self.balance, self.transactions)
        print s


def test_Account():
    a = Account('js', 1234,20)
    a.deposit(12)
    a.withdraw(3)
    expected = (29, 2)
    success = (a.balance,a.transactions) == expected
    assert success

if __name__ == '__main__':
    a = Account('js', 1234, 20)
    a.deposit(10)
    a.dump()
    test_Account()
	
	
"""

[emilyd@sudur kap7]$ python Account2.py
js, 1234, balance: 30, transactions: 1


"""	
 