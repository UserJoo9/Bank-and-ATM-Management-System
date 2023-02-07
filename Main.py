from Bank import Bank
import os

print("Welcome to e-Bank")
while 1:
    print("\nMain Menu")
    print("1- Login")
    print("2- Create Account")
    print("3- Exit")
    op = input("\nChoose you want: ")
    if op.upper() == '1':
        id = None
        user = None
        pwd = '!'
        print("\n!! Note: Type '!' In Any Field To Edit Refill Fields")
        while id == '!' or user == '!' or pwd == '!':
            id = str(input("\nEnter Account ID: "))
            user = str(input("Enter Account Name: "))
            pwd = str(input("Enter Account Password: "))
        b1 = Bank()
        b1.setUserID(id)
        b1.getData()
        if b1.getName() == user and b1.getPassword() == pwd and b1.getUserID() == id:
            b1.describe('')
            while os.path.exists(f'new acc {id}.txt'):
                print("\n*** Dashboard ***")
                print("1# Describe")
                print("2# Withdraw")
                print("3# Deposit")
                print("4# Change Password")
                print("5# Delete Account")
                print("6# Logout")
                select = input("Select: ")
                if select == '1':
                    print("Do You Want To Show Password?, Type (Y) For Yes")
                    sw = input(">> ")
                    if sw.upper() == 'Y':
                        b1.describe('normal')
                    else:
                        b1.describe('')
                elif select == '2':
                    b1.withdraw()
                elif select == '3':
                    b1.deposit()
                elif select == '4':
                    b1.changePwd()
                elif select == '5':
                    b1.deleteAcc()
                elif select == '6':
                    cls = '\n' * 100000
                    print(cls)
                    break
                else:
                    print("Choice not available!")
        else:
            print("Wrong Account Data!")
    elif op.upper() == '2':
        print("\nCreate e-Bank Account")
        id = ''
        name = ''
        password = ''
        b1 = Bank()
        b1.createAcc()
    elif op.upper() == '3':
        break
    else:
        print("\nUnknown Choice")

print("Thank You 😊")
