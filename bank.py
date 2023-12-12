import csv
import random

# Dictionaries for account management
Account = {}
Client = {}
ClientAccount = {}

# Function to add a new client
def addClient(numCl, MPC, numC, SoldeC):
    Client[numCl] = MPC
    Account[numC] = SoldeC
    ClientAccount[numCl] = numC

# Function to remove a client
def removeClient(numC):
    if numC in ClientAccount.values():
        numCl = [k for k, v in ClientAccount.items() if v == numC][0]
        del Client[numCl]
        del Account[numC]
        del ClientAccount[numCl]
        print(f"Client with account number {numC} removed.")
    else:
        print(f"Account number {numC} not found.")

# Function to modify a client's password
def modifyClientPassword(numCl, newMPC):
    if numCl in Client:
        Client[numCl] = newMPC
        print(f"Password for client {numCl} modified.")
    else:
        print(f"Client {numCl} not found.")

# Function to deposit money into an account
def deposit(numCl, amount):
    if numCl in ClientAccount:
        numC = ClientAccount[numCl]
        Account[numC] += amount
        print(f"Deposited {amount} Dh into account {numC}.")
    else:
        print(f"Client {numCl} not found.")

# Function to withdraw money from an account
def withdraw(numCl, amount):
    if numCl in ClientAccount:
        numC = ClientAccount[numCl]
        if Account[numC] >= amount:
            Account[numC] -= amount
            print(f"Withdrew {amount} Dh from account {numC}.")
        else:
            print("Insufficient funds.")
    else:
        print(f"Client {numCl} not found.")

# Lambda function to generate an account number
generateAccountNumber = lambda numCl: int(f"{numCl}{random.randint(0, 100)}")

# Function to write client data to a CSV file
def writeToCSVFile(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ClientNumber', 'SecretCode'])
        for numCl, MPC in Client.items():
            writer.writerow([numCl, MPC])

# Function to manipulate data structures and create list, tuple, and set
def manipulateDataStructures():
    accountNumbersList = list(Account.keys())
    accountNumbersTuple = tuple(Account.keys())
    accountNumbersSet = set(Account.keys())
    return accountNumbersList, accountNumbersTuple, accountNumbersSet

# Main program
while True:
    print("\nBank Management System Menu:")
    print("1. Agent Menu")
    print("2. Client Menu")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print("\nAgent Menu:")
        print("1. Add a Client")
        print("2. Remove a Client")
        print("3. Exit")

        agentChoice = input("Enter your choice (1/2/3): ")

        if agentChoice == '1':
            numCl = int(input("Enter client number: "))
            MPC = input("Enter secret code: ")
            numC = generateAccountNumber(numCl)
            SoldeC = float(input("Enter initial balance: "))
            addClient(numCl, MPC, numC, SoldeC)
            print(f"Client added with account number {numC}.")

        elif agentChoice == '2':
            numC = int(input("Enter account number to remove: "))
            removeClient(numC)

        elif agentChoice == '3':
            break

    elif choice == '2':
        print("\nClient Menu:")
        print("1. Modify Password")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        clientChoice = input("Enter your choice (1/2/3/4): ")

        if clientChoice == '1':
            numCl = int(input("Enter your client number: "))
            newMPC = input("Enter new secret code: ")
            modifyClientPassword(numCl, newMPC)

        elif clientChoice == '2':
            numCl = int(input("Enter your client number: "))
            amount = float(input("Enter amount to deposit: "))
            deposit(numCl, amount)

        elif clientChoice == '3':
            numCl = int(input("Enter your client number: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw(numCl, amount)

        elif clientChoice == '4':
            break

    elif choice == '3':
        writeToCSVFile('client_data.csv')
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
