import time
import sys

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def loading_animation(self):
        bar_width = 20
        sys.stdout.write("[%s]" % (" " * bar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (bar_width + 1))

        for i in range(bar_width):
            time.sleep(0.1)  # Simulating some task
            sys.stdout.write("-")
            sys.stdout.flush()

        sys.stdout.write("]\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposit of ${amount} successful. New balance: ${self.balance}')
        else:
            print('Invalid deposit amount.')

    def cash_out(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal of ${amount} successful. New balance: ${self.balance}')
        else:
            print('Withdrawal not allowed. Insufficient funds.')

    def check_balance(self):
        print(f'Current balance of {self.holder}\'s account: ${self.balance}')
