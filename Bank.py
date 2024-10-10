from collections import defaultdict
from pprint import *
class Account:
    database = defaultdict(dict)
    def __init__(self,name,dob,aadhar,address,mobileno,balance):
        self.id = aadhar #aadhar number acts as Bank number.
        self.name = name
        self.dob = dob
        self.aadhar = aadhar
        self.address = address
        self.mobileno = mobileno
        self.balance = balance
        self.transactions = []   #stores the transactions
        temp = {} #dictionary to hols acc information
        for i in ['name', 'dob', 'aadhar', 'address', 'mobileno', 'balance']:
            temp[i] = eval(f'self.{i}')
        self.database[self.id] = temp
        self.database[self.id]['transactions'] = self.transactions
        
def addTransaction(self,transaction_detail):
    self.transactions.append(transaction_detail)
    
def create_account(name, dob, aadhar, address, mobileno, balance):
    return Account(name, dob, aadhar, address, mobileno, balance)

print("Welcome to People's Bank")
while True:
    choice = int(input("\n1. Create your account\n2. View Account Details by Accno\n3.Deposit\n4.Withdraw\n5.Fund Transfer\n6.Print Transactions\n7.Exit\nEnter your choice = "))
    #creation of bank account
    if choice == 1:
        name = input("Enter your name = ")
        dob = input("ENter your Date of Birth (DD-MM-YYYY)= ") 
        aadhar = input("Enter your Aadhar number = ")
        address = input("Enter your Address = ")
        mobileno = int(input("Enter your Mobile Number = "))
        balance=0
        print("Your Account number is = ",aadhar)
        account = Account(name, dob, aadhar, address, mobileno, balance)
    #view acocunt details
    elif choice == 2:
        aadhar = input("Enter your account number = ")
        if aadhar not in Account.database:
            print("Account not found")
        else:
            pprint(Account.database[aadhar])
    #deposit money
    elif choice == 3:
        aadhar = input("Enter your account number = ")
        if aadhar not in Account.database:
            print("Account not found")
        else:
            amount = int(input("Enter the amount how much you want to deposit  = "))
            Account.database[aadhar]['balance']+=amount
            print("Current balance = ",Account.database[aadhar]['balance'])
            Account.database[aadhar]['transactions'].append(f"Deposited {amount}. Balance: {Account.database[aadhar]['balance']}")
            #Log the transactions
    #withdraw money
    elif choice == 4:
        aadhar = input("Enter your account number = ")
        if aadhar not in Account.database:
            print("Account not found")
        else:
            Amount = int(input("Enter the amount how much you want to withdraw = "))
            if Amount > Account.database[aadhar]['balance']:
                print("Sorry! you cannot  withdraw coz you have low balance......")
            else:
                print("After withdrawing your current balance is ",Account.database[aadhar]['balance']-Amount)
                Account.database[aadhar]['transactions'].append(f"Withdrawn {amount}. Balance: {Account.database[aadhar]['balance']}")  
                #Log the transactions
    elif choice == 5:
        user1=input("Enter your accno = ")
        user2=input("enter the accno of person for whom you want to transfer the amount = ")
        if user1 not in Account.database or user2 not in Account.database:
            print("Enter valid Account number.....")
        else:
            amount=int(input(f"Hi {user1}, Enter the amount  = "))
            print("Before Transfer, Your balance is = ",Account.database[user1]['balance'])
            if Account.database[user1]['balance']>amount:
                print("Sorry You don't have enough amount to Transfer....")
            else:
                Account.database[user1]['balance']-=amount
                Account.database[user2]['balance']+=amount
                print("Transfer succesfully done, Your balance is = ",Account.database[user1]['balance'])
                Account.database[user1]['transactions'].append(f"Transfered {amount} to {Account.database[user2]['name']}. Balance:{Account.database[user1]['balance']}")
                Account.database[user2]['transactions'].append(f"Recieved {amount} from {Account.database[user1]['name']}. Balance:{Account.database[user2]['balance']}")
                #Log the transactions
    elif choice==6:
        aadhar = input("Enter your accno to view transactions = ")
        if aadhar in Account.database:
                if 'transactions' in Account.database[aadhar]:
                    print("Transaction History....")
                    for transaction in Account.database[aadhar]['transactions']:
                        print(transaction)
                else:
                    print("No transactions found for this account")
        else:
            print("Enter valid account details.....")
    elif choice == 7:
        exit(0)