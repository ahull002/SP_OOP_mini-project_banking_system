# Object Orientied Programming-Banking-System
![Design Blocks](https://images.unsplash.com/photo-1523839699072-5ec088b61a21?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=2250&q=80)
Image by: Erol Ahmed

## Project Setup

We regularly interact with banks in our day-to-day lives but rarely think about the systems that power them. Banks power global finance, and the online information technology systems that enable these systems are incredibly complex.

## What is this?
This program is an example model of a banking system. We have designed the banking system using Python Object Oriented Programming (OOP) techniques. 

## How to use this?

1. Open the main.py file

2. The program presents the user with three options: 

> * 1. Open a new bank account
> * 2. Access existing bank account
> * 3. Exit terminal

Note:
- If the user chooses option 1: Open a new bank account
> * A prompt for name, address, account, we pass the deposit to the client's class in the client.py program.
> * The system creates a unique user account number with a five-digit number using random numbers between 10000 and 99999.
> * Account creates successfully, and we provide the user with a five-digit account number.


- If the user chooses option 2: Access existing bank account
> * The program provides a prompt for a name and an account number.
> * The system validates the authorization of the users' credentials against the authentication function within the bank class in the bank.py program.
> * if Authentication is OK, we grant the user access to the accounts menu where they can: withdraw, deposit, get the balance via the client class (client.py), or exit the account window. 
> * if Authentication fails, the user is presented with a security message and redirected to account login.


- If the user chooses option 3: Exit terminal
> * The program presents the user a message as the session terminates.


## Testing & Development

If you would like to work on this application, we'd love your pull requests and tickets on GitHub!

1. If you open up a ticket, please make sure it describes the problem and or feature request fully.
2. If you send us a pull request, make sure you add a test for what you completed.
_____
