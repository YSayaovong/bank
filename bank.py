from abc import ABC, abstractmethod

# Abstract class Bank
class Bank(ABC):

    # Method basicinfo()
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"

    # Abstract method withdraw()
    @abstractmethod
    def withdraw(self, amount):
        pass

# Derived class Swiss inheriting from Bank
class Swiss(Bank):

    # Constructor initializing bal to 1000
    def __init__(self):
        self.bal = 1000

    # Overridden method basicinfo()
    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"

    # Overridden method withdraw()
    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        else:
            self.bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New balance: {self.bal}")
            return self.bal

# Test cases
if __name__ == "__main__":
    swiss_bank = Swiss()
    print(swiss_bank.basicinfo())  # Should print "This is the Swiss Bank" and return "Swiss Bank: 1000"
    swiss_bank.withdraw(30)        # Should print "Withdrawn amount: 30" and "New balance: 970"
    swiss_bank.withdraw(2000)      # Should print "Insufficient funds"
