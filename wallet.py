from flask import Flask

balance = 750

def primary_function():

    global balance

    print("")
    print("           Welcome, the main menu is displayed below:")
    print("")
    print("#################################")
    print(" 1 : Check your balance")
    print("")
    print(" 2 : Make a deposit")
    print("")
    print(" 3 : Make a withdrawal")
    print("")
    print(" 4 : Exit this Terminal")
    print("#################################")

    selection = int(input("Make a selection when ready: "))

    if selection == 666:
        print("#################################")
        print("#################################")
        print("#################################")
        print("#################################")
        print("#################################")
        freeze_key = input("  You have frozen this terminal.\n  Your access has been revoked.\n  Exit by entering any key.")
        exit
    elif selection == 1:
        input(f"Your current balance is:   ${balance}\nEnter any key to return to the main menu")
        primary_function()
    elif selection == 2:
        deposited_amount = int(input(f"How much are you wanting to deposit today? :   $"))
        new_total = deposited_amount + balance
        balance = new_total
        input(f"Deposit successful; Your new balance is  ${new_total}\nEnter any key to return to the main menu.")
        primary_function()
    elif selection == 3:
        withdrawn_amount = int(input("How much would you like to withdraw? :   $"))
        new_total = balance - withdrawn_amount
        balance = new_total
        input(f"Withdrawal successful; Your new balance is  ${new_total}\nEnter any key to return to the main menu.")
        primary_function()
    elif selection == 4:
        exit
    # elif selection == str(input("")):
    #     input("Your selection is not recognized by this system.\nPlease ensure your input is a number in the above menu. ")
    else:
        input("Your selection is not recognized by this system.\nPlease ensure your input is a number in the above menu. ")
        primary_function()

primary_function()
        