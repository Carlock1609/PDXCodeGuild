#! python3
# instance variables are instances fro the class that get instantiated
# a_dog = Dog()

class ATM():
    def __init__(self, 
                balance=0,
                ):
        self.balance = balance

    def check_balance(self):
        total_balance = 0
        return total_balance

    def get_deposit(self):
        amount = int(input("Please enter in a dollar amount: "))
        return f"You deposited ${amount}"
    # Use this 
    def check_withdrawel(self,amount):
        if amount >= self.balance:
            return False
        else:
            return True

    def get_withdraw(self):
        amount = int(input("Please enter in a dollar amount: "))
        return f"You withdrew ${amount}"

    def print_transactions(self):
        trans_list = []
        return trans_list

def main():
    my_atm = ATM(balance=1500)

    trans = my_atm.print_transactions()
    balance = my_atm.check_balance()
    # figuring out how to get mutlple inputs to add to trans
    # why is the user input AMOUNT being called everytime, and functions fail without it
    # while True:
    #     amount = int(input("Please enter in a dollar amount: "))

    # MAKE LOOP WITH AMOUNT IN EACH IF STATEMENT
    # LOOK UP HOW TO STRUCTURE THIS MESS
    
    while True:
        user_input = input("What would you like to do (Deposit, Withdraw, Check Balance, History): ").lower()

        if user_input == "deposit":
            deposit = my_atm.get_deposit()
            print(f"\n{deposit}")
            print(trans.append(deposit))
        elif user_input == "withdraw":
            withdraw = my_atm.get_withdraw()
            print(f"\n{withdraw}")
            print(trans.append(withdraw))
        elif user_input == "check balance":
            print(f"Your total balance is ${balance}")
            print(trans.append(balance))
        elif user_input == "history":
            print(f"Your transactions are {trans}")
        else:
            print("\nPlease enter in Deposit, Withdraw, Check Balance or History: ")
            print(user_input)



main()

# print(trans.append(deposit)) THIS WORKS FOR ADDING TO LIST