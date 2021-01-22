shutdown = False

balance = float(700.50)

format(balance, '.2f')


def printbalance():
    '''this prints the Balance to the user'''
    return (balance)


def fastcash():
    global balance
    fast = 50
    '''determines if the user's account has at least 50$, then draws that out'''
    if balance < (50):
        print("Sorry, but you do not have enough funds to process this transcaction.")
    else:
        print("Dispensing fast cash ($50)")
        balance -= fast


def deposit():
    '''This adds the user inputted float to the balance'''
    global balance
    deposited = float(input("How much would you like to deposit today?: "))
    if deposited <= (0):
        print("That's not a valid amount.")
    else:
        balance += deposited
        print("Deposit complete. Balance updated")


def withdrawbalance():
    '''This function withdraws funds from the user's account balance. If the balance is too low, it returns an error.'''

    global balance
    withdraw = int(
        input("How much would you like?"))
    if withdraw < balance:
        print("Transaction complete. Dispensing money.")
        balance -= withdraw
    else:
        print("Insufficient funds.")


while (shutdown == False):
    # added in to keep refreshing the menu after an action is made/input is made

    print(" ")
    print("MENU")
    print(" ")
    print("1 = Deposit")
    print("2 = Withdrawal")
    print("3 = View Balance")
    print("4 = Get Fast Cash ($50)")
    print("5 = Quit Program")
    userchoice = int(input("What would you like to do?: "))

    if (userchoice == 1):
        deposit()

    elif (userchoice == 2):
        withdrawbalance()

    elif (userchoice == 3):
        printbalance()
        print("Your current balance is: ")
        print(balance)

    elif (userchoice == 4):
        fastcash()

    elif (userchoice == 5):
        print("Thanks for banking with us!")
        quit
        shutdown = True

    else:
        print("Error")
