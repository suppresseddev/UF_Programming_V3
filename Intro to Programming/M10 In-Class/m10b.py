import base_classes as base
class SecureAccount(base.Account):
    def __init__(self, password):
        super().__init__()
        self.key = password
    def get_balance(self, password):
        if password == self.key:
            return super().get_balance()
        else:
            print("Incorrect password")
    def deposit(self, amount, password):
        if password == self.key:
            return super().deposit(amount)
        else:
            print("Incorrect password")
    def withdraw(self, amount, password):
        if password == self.key:
            return super().withdraw(amount)
        else:
            print("Incorrect password")
class MemoryCalculator(base.Calculator):
    def __init__(self):
        super().__init__()
        self.result = 0
    def add(self, x, y):
        if x == 'RESULT':
            x = self.result
        if y == 'RESULT':
            y = self.result
        self.result = super().add(x, y)
        return self.result
    def sub(self, x, y):
        if x == 'RESULT':
            x = self.result
        if y == 'RESULT':
            y = self.result
        self.result = super().sub(x, y)
        return self.result
class ImprovedFraction(base.Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
    def add(self, other):
        if type(other) is int:
            k = ImprovedFraction(int(other), 1)
            return super().add(k)
        else:
            return super().add(other)
    def multiply(self, other):
        if type(other) is int:
            k = ImprovedFraction(int(other), 1)
            return super().multiply(k)
        else:
            return super().multiply(other)
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.multiply(other)
    def __str__(self):
        return f"{super().get_numerator()}/{super().get_denominator()}"