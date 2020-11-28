# Simple-Banking-System

![Design Blocks](https://images.unsplash.com/photo-1523839699072-5ec088b61a21?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=2250&q=80)
Image by: Erol Ahmed

## Project Setup

We regularly interact with banks in our day-to-day lives, but rarely think about the systems that power them. Banks power global finance, and the online systems that enable these systes are incredibly complex.

In this Springboard project I have created a simpler version of a banking system. I have designed the banking system using Python Object Oreiented Programming (OOP) techniques. In my simple bank model, I have included the following entities; customers, accounts, employees, and loans and credit cards services. Each of these entities have distinct properties and the relevant properties are defined below.

__Customer records could have a:__
1. __Entity:__ first and last name (Properties: str)
2. __Entity:__ address (Properties: str)
3. __Entity:__ deposit capability (Properties: float)
4. __Entity:__ withdrawal capability (Properties: float)
5. __Entity:__ balance capability (Properties: float)
6. __Entity:__ accounts (Properties: checking/savings)


__Simple Conceptual Design:__
- Initially, an instance of the bank class is created, with a name and a database, represented by a list of dictionaries.

- The user can create a new bank account, open an existing one, or exit the program.

- If the user chooses to create an account, a prompt for a name and an initial deposit are passed to the client's init method.

- The system creates a unique user account number with a five-digit number using random numbers between 10000 and 99999.

- The system adds the client to the bank class after the instantiation of the Client object.

- After creating the account, the user can choose to create another account or take away funds from an existing one. If the user selects the second option, the user authenticates the account with a name and the account number. The two arguments passed to the bank class's authentication method. If such credentials exist in the bank database, the system creates a variable called current_customer.

- Finally, the user can do operations with his account: withdraw, deposit, check balance, or exit to the main menu.
_____
