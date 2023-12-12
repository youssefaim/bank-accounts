# bank-accounts
The Bank Management System is a Python program designed to facilitate the management of accounts within a bank. The system incorporates both agent and client functionalities, offering a range of operations to efficiently handle account-related tasks.

Agent Menu:

Add a Client:

The agent can add a new client to the system, assigning a unique client number, a secret code for security access, and generating a random account number with an initial balance.
Remove a Client:

The agent can remove an existing client from the system, prompting for the account number to be deleted.
Exit:

Allows the agent to exit the system.
Client Menu:

Modify Password:

Clients can modify their secret code for enhanced security.
Deposit Money:

Clients can deposit a specified amount into their account.
Withdraw Money:

Clients can withdraw a specified amount from their account, ensuring that the withdrawal amount does not exceed the account balance.
Exit:

Allows clients to exit the system.
Additional Features:

Generate Account Number (Lambda Function):

The program uses a lambda function to generate a unique account number for each client based on their client number and a random number between 0 and 100.
Write to CSV File:

The program provides functionality to write client data, including client number and secret code, to a CSV file named 'client_data.csv' for future reference.
Data Structure Manipulation:

The program includes a function to manipulate data structures, creating a list, tuple, and set of account numbers from the dictionary representing client-account associations.
Usage:

Run the program.
Navigate through the agent or client menus by entering the corresponding choices.
Perform various operations such as adding or removing clients, modifying passwords, depositing, and withdrawing money.
Exit the program when the tasks are complete.
