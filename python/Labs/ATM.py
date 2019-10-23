#! python3
# instance variables are instances fro the class that get instantiated
# a_dog = Dog()

class ATM():
    def __init__(self, 
                balance=0,
                print_transactions=[],
                ):
        self.balance = balance
        self.print_transactions = []

    def check_balance(self):
        return self.balance

    def get_deposit(self, amount):
        self.balance += amount
        self.print_transactions.append(f"You deposited ${amount}")
        return self.balance
    # Use this 
    def check_withdrawel(self, amount):
        return amount > self.balance

    def get_withdraw(self, amount):
        self.balance -= amount
        self.print_transactions.append(f"You withdrew ${amount}")
        return self.balance

    def get_transactions(self,):
        return self.print_transactions

def get_amount():
    amount = int(input("Please enter in a dollar amount: "))
    return amount

def main():
    my_atm = ATM(balance=1500,
                print_transactions=[])

    while True:
        user_input = input("What would you like to do (Deposit, Withdraw, Check Balance, History): ").lower()

        if user_input == "deposit":
            my_atm.get_deposit(get_amount())
        elif user_input == "withdraw":
            amount = get_amount()
            if my_atm.check_withdrawel(amount) == False:
                my_atm.get_withdraw(amount)
            else:
                print("You do not have enough money. Please feed me more dollars.")
        elif user_input == "check balance":
            print(f"Your total balance is ${my_atm.check_balance()}")
            print((my_atm.check_balance()))
        elif user_input == "history":
            print(f"Your transactions are {my_atm.get_transactions()}")
        else:
            print("\nPlease enter in Deposit, Withdraw, Check Balance or History: ")
main()
