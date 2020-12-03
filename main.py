## Import files
from client import Client
from bank import Bank

# Setting Bank function to a variable
bank = Bank()

# Spelling out welcome banner
welcome = "Welcome to {}!".format(bank.name)
print(f' --------------------------------------------\n {welcome}\n --------------------------------------------')

# Running input prompt
running = True
while (running==True):
    print()
    print("""Choose an option:
    
    1. Open a new bank account
    2. Access existing bank account
    3. Exit terminal
    """)
    
    # Build menu selector
    choice = int(input("1, 2 or 3: "))

    # Build outer try statment to encapsulate the program
    try:
        # Selected if option 1: Open new bank account is chosen
        if choice == 1:
            print(f' \nTo create a new account, please provide the information below.\n ')
            client = Client(input("Name: "), str(input("Address: ")), str(input("Account Type (checking or savings): ")), float(input("Deposit amount: ")))
            response=bank.update_db(client)
            
            # Validate that account_number matches
            if (response==True):
                client_account = client.account['account_number']
                print(f'_______________________________________________________________\n<<Account created successfully! Your account number is: {client_account}>>')

        # Selected if option 2: Access existing bank account
        elif choice == 2:
            
            # Build inter try statement to access account and validate account_number
            try:
                print(f' \nTo access your account, please enter your access information.\n ')
                name = input("Name: ")
                account_number = int(input("Account number: "))
            except Exception:
                print("Your account number is a five digit number")

            current_client = bank.authentication(name, account_number)
            if current_client:
                print()
                print("Welcome {}!".format(current_client.account['name']))
                acc_open = True
                while (acc_open==True):
                    print()
                    print("""Choose an option:

        1. Withdraw
        2. Deposit
        3. Balance
        4. Exit Account Window
                        """)
                    acc_choice = int(input("1, 2, 3 or 4: "))
                    
                    # Selected if sub-option 1: Withdraw
                    if acc_choice == 1: 
                        print()
                        
                        # Add in exception handling for withdrawal issues
                        try:
                            withdraw = int(input("Withdraw amount: "))
                            if (withdraw <= 0):
                                raise Exception()                            
                            else:
                                current_client.withdraw(withdraw)
                        except Exception:
                            print("Your withdrawal amount should be a positive integer.")
                    
                    # Selected if sub-option 2: Deposit
                    elif acc_choice == 2: 
                        print()
                        
                        # Add in exception handling for withdrawal issues
                        try:
                            deposit = int(input("Deposit amount: "))
                            if (deposit <= 0):
                                raise Exception("")
                            else: 
                                current_client.deposit(deposit)
                        except Exception:
                            print("Your deposit amount should be a positive integer.")
                    
                    # Selected if sub-option 3: Balance
                    elif acc_choice == 3:  
                        print()
                        current_client.balance()
                    
                    # Selected if sub-option 4: Exit Account Window
                    elif acc_choice == 4:  
                        current_client = ''
                        acc_open = False    
                    else:
                        print("only entering 1,2, 3 and 4 is allowed")
            
            # Inner loop else statement if authentication fails
            else:
                print(f' \n-Authentication failed!\n-Reason: Account not found.\n----\nDo you want to try again? If not, ')
                continue

        # Selected if option 3: Exit the terminal
        elif choice == 3:
            running = False
        
        # Outer loop else to catch failures if anything is selected outside 1 through 3
        else:
            print("only entering 1,2 and 3 is allowed")
        
    # If anything breaks within the try statement (i.e. an individual tries to pass in a letter for an account number) run this general exception
    except Exception:
        print('-- We apologize for the inconvenience. --\n-- Due to security reasons suspicious activity has occured and we are terminating this session. --\nPlease try back at a later time.')
    
    # Do this no matter what happens within the program
    finally:
        print(f'==========================================\nThank you for allowing us to service you!\n==========================================')