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

    def get_deposit(self,amount):
        return f"You deposited ${amount}"
    
    def check_withdrawel(self,amount):
        if amount >= self.balance:
            return False
        else:
            return True

    def get_withdraw(self,amount):
        return f"You withdrew ${amount}"

    def print_transactions(self):
        trans_list = []
        return trans_list

def main():
    my_atm = ATM(balance=1500)

    # figuring out how to get mutlple inputs to add to trans
    # why is the user input AMOUNT being called everytime, and functions fail without it
    # while True:
    #     amount = int(input("Please enter in a dollar amount: "))

    # MAKE LOOP WITH AMOUNT IN EACH IF STATEMENT
    while True:
        user_input = input("What would you like to do (Deposit, Withdraw, Check Balance, History")

        amount = int(input("Please enter in a dollar amount: "))
        balance = my_atm.check_balance()
        deposit = my_atm.get_deposit(amount)
        check_withdraw = my_atm.check_withdrawel(amount)
        withdraw = my_atm.get_withdraw(amount)
        trans = my_atm.print_transactions()

    # dict1 = {"Deposit": deposit,
    #         "Withdraw": withdraw,
    #         "Check Balance": balance,
    #         "History": trans,
    #         }

main()

# print(trans.append(deposit)) THIS WORKS FOR ADDING TO LIST