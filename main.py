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
while running:
    print()
    print("""Choose an option:
    
    1. Open a new bank account
    2. Access existing bank account
    3. Exit terminal
    """)

    choice = int(input("1, 2 or 3: "))

    # Selected if option 1: Open new bank account is chosen
    try:
        if choice == 1:
            print(f' \nTo create a new account, please provide the information below.\n ')
            client = Client(input("Name: "), str(input("Address: ")), str(input("Account Type (checking or savings): ")), float(input("Deposit amount: ")))
            bank.update_db(client)
            client_account = client.account['account_number']
            print(f'_______________________________________________________________\n<<Account created successfully! Your account number is: {client_account}>>')

        # Selected if option 2: Access existing bank account
        elif choice == 2:
            print(f' \nTo access your account, please enter your access information.\n ')
            name = input("Name: ")
            account_number = int(input("Account number: "))
            current_client = bank.authentication(name, account_number)
            if current_client:
                print()
                print("Welcome {}!".format(current_client.account['name']))
                acc_open = True
                while acc_open:
                    print()
                    print("""Choose an option:

        1. Withdraw
        2. Deposit
        3. Balance
        4. Exit Account Window
                        """)
                    acc_choice = int(input("1, 2, 3 or 4: "))

                    if acc_choice == 1: # Selected if sub-option 1: Withdraw
                        print()
                        current_client.withdraw(int(input("Withdraw amount: ")))
                    elif acc_choice == 2: # Selected if sub-option 2: Deposit
                        print()
                        current_client.deposit(int(input("Deposit amount: ")))
                    elif acc_choice == 3:  # Selected if sub-option 3: Balance
                        print()
                        current_client.balance()
                    elif acc_choice == 4:  # Selected if sub-option 4: Exit Account Window
                        current_client = ''
                        acc_open = False
            else:
                print(f' \n-Authentication failed!\n-Reason: Account not found.\n----\nDo you want to try again? If not, ')
                continue

        # Selected if option 3: Exit the terminal
        elif choice == 3:
            running = False
    
    # If anything breaks within the try statement (i.e. an individual tries to pass in a letter for an account number) run this general exception
    except Exception:
        print('-- We apologize for the inconvenience. --\n-- Due to security reasons suspicious activity has occured and we are terminating this session. --\nPlease try back at a later time.')
    
    # Do this no matter what happens within the program
    finally:
        print(f'==========================================\nThank you for allowing us to service you!\n==========================================')