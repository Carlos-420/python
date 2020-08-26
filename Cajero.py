import os
money = 1000
op = '0'


def DoR(cash):
    print("Press '1' for a deposit")
    print("Press '2' for a retire")
    op2 = input("So you want option....")
    if op2 == '1':
        print("So you decide deposit!")
        DorR = float(input("Enter the money to deposit: "))
        cash += DorR
        print(f"You deposit Q{DorR}")
        print(f"Now you have Q{cash:.2f}")
    elif op2 == '2':
        print("So you decide retire!")
        DorR = float(input("Enter the money to retire: "))
        if DorR > cash:
            print("You don't have enough money")
        if cash >= DorR:
            cash -= DorR
            print(f"You retire Q{DorR}")
            print(f"Now you have Q:{cash:.2f}")
    else:
        print("Incorrect option")
    return cash


while op != '3':
    print("**********Automatic Teller Machine**********")
    print("Which option you want?")
    print("Press '1' for do a deposit or a retire")
    print("Press '2' for see your amount of money available")
    print("Press '3' for exit")
    op = input("So you want option... ")
    if op == '1':
        os.system("cls")
        money = DoR(money)
        os.system("pause")
        os.system("cls")
    elif op == '2':
        os.system("cls")
        print(f"You have Q{money:.2f}")
        os.system("pause")
        os.system("cls")
    elif op == '3':
        os.system("cls")
        print("Thanks for use the ATM")
        print("GoodBye!")
        os.system("pause")
    else:
        os.system("cls")
        print("That option is not in the menu")
        os.system("pause")
        os.system("cls")
