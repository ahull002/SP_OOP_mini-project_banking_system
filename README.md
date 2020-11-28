# Object Orientied Programming-Banking-System
![Design Blocks](https://images.unsplash.com/photo-1523839699072-5ec088b61a21?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=2250&q=80)
Image by: Erol Ahmed

## Project Setup

We regularly interact with banks in our day-to-day lives, but rarely think about the systems that power them. Banks power global finance, and the online systems that enable these systems are incredibly complex.

## What is this?
An example model of a banking system. We have designed the banking system using Python Object Oreiented Programming (OOP) techniques. 

## How to use this?

1. Open the main.py file

2. The user is presented with three options: 

> * 1. Open a new bank account
> * 2. Access existing bank account
> * 3. Exit terminal

Note:
- If the user chooses option 1: Open a new bank account
> * A prompt for: name, address, account, deposit is passed to the client's class in the client.py program.
> * The system creates a unique user account number with a five-digit number using random numbers between 10000 and 99999.
> * Account is created successfully, and a five-digit account number is provided.


- If the user chooses option 2: Access existing bank account
> * A prompt for: name, and account number is provided
> * The system validates the authorization of the users' credential against the authentication function within the bank class in the bank.py program.
> * if Authentication is good the user is granted access to the accounts menu where they can: withdraw, deposit, get balance via the client class (client.py), or exit the account window. 
> * if Authentication is failed the user is presented with a security message and redirected to account login.


- If the user chooses option 3: Exit terminal
> * The session is terminated and the user is presented with a message


# Testing

1. TBD

# Development
If you would like to work on this application we’d love your pull requests and tickets on GitHub!

1. If you open up a ticket, please make sure it describes the problem and or feature request fully.
2. If you send us a pull request, make sure you add a test for what you added.
_____