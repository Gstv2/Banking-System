import os
from System_Bank import BankAccount

os.system("cls")
print(20 * "=-")
print(10 * " " + "Welcome to System Bank")
print(20 * "=-")
print("What is your name?")
user_name = input("Type your name: ")
user_account = BankAccount(user_name)

while True:
    print(20 * "=-")
    print(6 * " " + "How can I help you, {}\n".format(user_name))
    print( 20 * "=-")
    print("Options:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Cash Out")
    print("4. Exit")
    print(20 * "=-") 

    option = input("Choose an option (1/2/3/4): ")

    if option == "1":
        user_account.loading_animation()
        os.system("cls")
        user_account.check_balance()
    elif option == "2":
        deposit_amount = float(input("Type the amount to be deposited: "))
        user_account.loading_animation()
        os.system("cls")
        user_account.deposit(deposit_amount)
    elif option == "3":
        withdrawal_amount = float(input("Type the amount to be withdrawn: "))
        user_account.loading_animation()
        os.system("cls")
        user_account.cash_out(withdrawal_amount)
    elif option == "4":
        print("Exiting the system.")
        user_account.loading_animation()
        print("Thank you for using our services.")
        break
    else:
        print("Invalid option. Please try again.")
