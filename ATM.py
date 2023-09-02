# import required libraries
import time
import os

# define the ATM class
class ATM:
    def __init__(self, pin, balance=10000):
        # initialize the class variables
        self.pin = pin
        self.balance = balance

    # define the deposit function
    def deposit(self, amount):
        # check for invalid deposit amount
        if amount <= 0:
            print("Invalid amount. Please enter a positive amount.")
            return
        # update account balance after deposit
        self.balance += amount
        print(f"Deposit of Rs{amount:.2f} successful. Your new balance is Rs{self.balance:.2f}")

    # define the withdraw function
    def withdraw(self, amount):
        # check for invalid withdrawal amount
        if amount <= 0:
            print("Invalid amount. Please enter a positive amount.")
            return
        # check for insufficient balance
        if self.balance < amount:
            print("Insufficient balance. Please enter a lower amount.")
            return
        # update account balance after withdrawal
        self.balance -= amount
        print(f"Withdrawal of Rs{amount:.2f} successful. Your new balance is Rs{self.balance:.2f}")

    # define the check_balance function
    def check_balance(self):
        # display current account balance
        print(f"Your current balance is Rs{self.balance:.2f}")

# define the function to clear the screen
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# define the main function
def main():
    clear_screen()
    print("Welcome to the ATM machine!")

    # simulate card insertion
    time.sleep(1)

    # set the PIN and prompt the user to enter it
    pin = 7488
    print(f"Please enter your 4-digit PIN: ")
    attempts = 3
    while attempts > 0:
        user_pin = input("PIN: ")
        # check for invalid PIN
        if user_pin != str(pin):
            attempts -= 1
            print(f"Invalid PIN. You have {attempts} attempts remaining.")
            continue
        else:
            print("PIN accepted. You can now access your account.")
            break
    else:
        print(" Too many attempts . Please try again later.")
        return

    # create an ATM object and prompt the user for actions
    atm = ATM(pin)
    while True:
        print("Please select an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        # get user input and perform the selected action
        option = input("Option: ")
        if option == "1":
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif option == "2":
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif option == "3":
            atm.check_balance()
        elif option == "4":
            print("Thank you for using the ATM machine!")
            break
        else:
            print("Invalid option. Please enter a valid option.")


if __name__ == "__main__":
    main()
