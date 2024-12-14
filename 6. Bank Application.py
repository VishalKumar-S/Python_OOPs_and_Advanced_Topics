import random
import sys

class Bank:
    def __init__(self,acc_no,name,deposit):
        self.acc_no = acc_no
        self.name = name
        self.balance = deposit
    
    def deposit(self,amt):
        self.balance+=amt

    def withdraw(self,amt):
        self.balance-=amt


def acc_no_validation():
    print("Enter your account no: ")
    acc_no = str(input())
    try: 
        if acc_no in accounts:
            return accounts[acc_no]
    except:
        print("Sorry! Your account no is either invalid or doesn't exist")

    return False

def valid_amount():
    amt= int(input())
    while amt<0:
        print("Enter valid amount: ")
        amt= int(input())
    return amt

accounts = {}
print("Welcome to Vishal's Bank")
while True:
    print("Choose any of the options:\n 1-Account Creation \n 2- Deposit\n 3- Withdraw\n 4-Check Balance \n 5-Transfer Money \n 6-Account Information \n 7-Exit")
    print("Enter the option no:")
    try:
        option = int(input())
        if option == 1:
            print("Enter account holder's name:")
            name = str(input())
            print("Enter inital deposit amount:")
            deposit = valid_amount()
            acc_no = ''.join(str(random.randint(0,9)) for _ in range(5))
            accounts[acc_no] = Bank(acc_no,name,deposit)
            print("Thanks for joining in our Vishal's Bank family.\n Your account no is",accounts[acc_no].acc_no)

        elif option == 2:
            acc_no = acc_no_validation()
            if acc_no:
                print("Enter the amount to Deposit:")
                dep_amt = valid_amount()
                acc_no.deposit(dep_amt)
            

        elif option == 3:
            acc_no = acc_no_validation()
            if acc_no:
                print("Enter the amount to withdraw:")
                withdraw_amt = valid_amount()
                if withdraw_amt <= acc_no.balance:
                    acc_no.withdraw(withdraw_amt)
                    print("Your current balance is: ,",acc_no.balance)
                else:
                    print("Insufficient balance.")

        
        elif option == 4:
            acc_no = acc_no_validation()
            if acc_no:
                print("Your current balance is: ,",acc_no.balance)

        
        elif option == 5:
            print("Enter Sender's account no:")
            sender = acc_no_validation()
            if sender:
                print("Enter Receiver's account no:")
                receiver = acc_no_validation()
                if receiver:
                    print("Enter amount to transfer:")
                    transfer_amt = valid_amount()
                    if sender.balance >=transfer_amt:
                        sender.withdraw(transfer_amt)
                        receiver.deposit(transfer_amt)
                        print(f"Transferred successfuly, sender's account is debited {transfer_amt}. Current balance is {sender.balance}")
                    else:
                        print("Funds insufficient in the account")
                


        elif option == 6:
            acc_no = acc_no_validation()
            if acc_no:
                print("Account information is: ")
                print("Account no: ",acc_no.acc_no)
                print("Account holder name: ",acc_no.name)
                print("Balance: ",acc_no.balance)
        
        elif option == 7:
            print("Thanks for using our services. Have a nice day!!!")
            sys.exit()

        else:
            print("Enter valid option!!!")
        
        
    except ValueError:
        print("Please enter a valid option number!")
        continue
