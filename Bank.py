# import os
from customtkinter import *
from win32api import GetSystemMetrics
from PIL import Image

width = int(GetSystemMetrics(0) / 3)
height = int(GetSystemMetrics(1) / 6)
aspectRatio = f'{width}+{height}'


class Bank():

    def __init__(self):
        self.__id = "100"
        self.__userid = id
        self.__name = None
        self.__password = None
        self.__Dollarbalance = 0
        self.__LEbalance = 0

    # ------------------------------------------- START GUI -----------------------------------------------

    def ctkmessagbox_showinfo(self, parent, title, description):
        try:
            self.showinfo = CTkToplevel(parent)
        except:
            self.showinfo = CTkToplevel()
        self.showinfo.title(title)
        self.showinfo.resizable(False, False)
        self.AR = f'{int(GetSystemMetrics(0) / 3)}+{int(GetSystemMetrics(1) / 6)}'
        self.showinfo.geometry(self.AR)

        self.showinfoimage = CTkImage(light_image=Image.open("img/info.jpg"), dark_image=Image.open("img/info.jpg"),
                                      size=(30, 30))

        self.showinfo_Label = CTkLabel(self.showinfo, image=self.showinfoimage, text=" " + description,
                                       font=("roboto", 16, "bold"),
                                       width=300, compound="left")
        self.showinfo_Label.grid(row=0, column=0, columnspan=5, pady=30, padx=20)

        self.showinfo_Button = CTkButton(self.showinfo, text="OK", width=80, font=("roboto", 10, "bold"),
                                         command=self.showinfo.destroy)
        self.showinfo_Button.grid(row=1, column=4, pady=10)

    def ctkmessagbox_showerror(self, parent, title, description):
        try:
            self.showerror = CTkToplevel(parent)
        except:
            self.showerror = CTkToplevel()
        self.showerror.title(title)
        self.showerror.resizable(False, False)
        self.AR = f'{int(GetSystemMetrics(0) / 3)}+{int(GetSystemMetrics(1) / 6)}'
        self.showerror.geometry(self.AR)

        self.showerrorimage = CTkImage(light_image=Image.open("img/!-mark.png"),
                                       dark_image=Image.open("img/!-mark.png"),
                                       size=(25, 25))

        self.showerror_Label = CTkLabel(self.showerror, image=self.showerrorimage, text=" " + description,
                                        font=("roboto", 16, "bold"),
                                        width=300, compound="left")
        self.showerror_Label.grid(row=0, column=0, columnspan=5, pady=30, padx=20)

        showerror_Button = CTkButton(self.showerror, text="OK", width=80, font=("roboto", 10, "bold"), fg_color="brown",
                                     hover_color="red", command=self.showerror.destroy)
        showerror_Button.grid(row=1, column=4, pady=10)

    def mainMenu(self):
        self.root = CTk()
        self.root.title("e-Bank")
        self.root.resizable(False, False)
        self.root.geometry(aspectRatio)

        self.mainFrame = CTkFrame(self.root)
        self.mainFrame.pack(pady=20, padx=20)

        self.greetingsLabel = CTkLabel(self.mainFrame, text="Welcome to e-Bank", font=("roboto", 22, 'bold'),
                                       width=400, height=50)
        self.greetingsLabel.pack(pady=10, padx=20)

        self.loginButton = CTkButton(self.mainFrame, text="Login", font=("roboto", 18, 'bold'), width=300, height=40,
                                     command=self.loginUI)
        self.loginButton.pack(pady=(0, 10), padx=20)

        self.createAccountButton = CTkButton(self.mainFrame, text="Create Account", font=("roboto", 18, 'bold'),
                                             width=300,
                                             height=40, command=self.createAccUI)
        self.createAccountButton.pack(pady=(0, 10), padx=20)

        self.exitButton = CTkButton(self.mainFrame, text="Exit", font=("roboto", 15, 'bold'), width=200, height=30,
                                    fg_color="brown", hover_color="red", command=self.root.destroy)
        self.exitButton.pack(pady=20, padx=20)

        self.root.mainloop()

    def loginUI(self):
        self.login = CTkToplevel(self.root)
        self.login.title("Login")
        self.login.resizable(False, False)
        self.login.geometry(aspectRatio)

        self.loginFrame = CTkFrame(self.login)
        self.loginFrame.pack(pady=20, padx=20)

        self.loginLabel = CTkLabel(self.loginFrame, text="Login", width=400, height=50, font=("roboto", 22, "bold"))
        self.loginLabel.pack(pady=10, padx=20)

        self.loginIdEntry = CTkEntry(self.loginFrame, placeholder_text="ID", font=("roboto", 18, "bold"), width=300)
        self.loginIdEntry.pack(pady=(0, 10), padx=20)

        self.loginNameEntry = CTkEntry(self.loginFrame, placeholder_text="Username", font=("roboto", 18, "bold"),
                                       width=300)
        self.loginNameEntry.pack(pady=(0, 10), padx=20)

        self.loginPassEntry = CTkEntry(self.loginFrame, placeholder_text="Password", font=("roboto", 18, "bold"),
                                       width=300,
                                       show="*")
        self.loginPassEntry.pack(pady=(0, 10), padx=20)

        self.loginButton = CTkButton(self.loginFrame, text="Login", font=("roboto", 18, "bold"), width=300, height=30,
                                     command=lambda: self.userLogin(self.loginIdEntry.get(), self.loginNameEntry.get(),
                                                                    self.loginPassEntry.get()))
        self.loginButton.pack()

        self.loginExitButton = CTkButton(self.loginFrame, text="Exit", font=("roboto", 15, "bold"), width=100,
                                         height=20,
                                         fg_color="brown", hover_color="red", command=self.login.destroy)
        self.loginExitButton.pack(pady=20)

    def createAccUI(self):
        self.create = CTkToplevel(self.root)
        self.create.title("Create Account")
        self.create.resizable(False, False)
        self.create.geometry(aspectRatio)

        self.createFrame = CTkFrame(self.create)
        self.createFrame.pack(pady=20, padx=20)

        self.createLabel = CTkLabel(self.createFrame, text="Create Account", font=("roboto", 22, "bold"), height=50,
                                    width=400)
        self.createLabel.pack(pady=10, padx=20)

        self.createIdEntry = CTkEntry(self.createFrame, placeholder_text="ID (Auto fill)", width=300)
        self.createIdEntry.pack(pady=(0, 10), padx=20)
        self.createIdEntry.configure(state="disabled")

        self.createUsernameEntry = CTkEntry(self.createFrame, placeholder_text="Username", width=300)
        self.createUsernameEntry.pack(pady=(0, 10), padx=20)

        self.createPassEntry = CTkEntry(self.createFrame, placeholder_text="Password", width=300,
                                        show="*")
        self.createPassEntry.pack(pady=(0, 10), padx=20)

        self.reCreatePassEntry = CTkEntry(self.createFrame, placeholder_text="Password again", width=300,
                                          show="*")
        self.reCreatePassEntry.pack(pady=(0, 10), padx=20)

        self.createAccButton = CTkButton(self.createFrame, text="Submit", font=("roboto", 18, "bold"), width=300,
                                         height=30)
        self.createAccButton.pack(pady=(0, 10), padx=20)

        self.exitCreateAccButton = CTkButton(self.createFrame, text="Exit", font=("roboto", 15, "bold"), width=200,
                                             height=20,
                                             fg_color="brown", hover_color="red", command=self.create.destroy)
        self.exitCreateAccButton.pack(pady=10, padx=20)

    def dashboard(self):
        self.login.destroy()
        self.board = CTkToplevel(self.root)
        self.board.title("Account Details")
        self.board.resizable(False, False)
        self.board.geometry(aspectRatio)

        self.bordFrame = CTkFrame(self.board)
        self.bordFrame.pack(padx=20, pady=20)

        self.boardLabel = CTkLabel(self.bordFrame, text="Dashboard & Control", font=("roboto", 22, "bold"), width=400,
                                   height=50)
        self.boardLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        self.idLabel = CTkLabel(self.bordFrame, text=f"ID: {b1.getUserID()}", font=("roboto", 18, "bold"))
        self.idLabel.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.nameLabel = CTkLabel(self.bordFrame, text=f"NAME: {b1.getName()}", font=("roboto", 18, "bold"))
        self.nameLabel.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.egpBalanceLabel = CTkLabel(self.bordFrame, text=f"EGP: {b1.getEgpt()}.LE", font=("roboto", 18, "bold"),
                                        text_color="orange")
        self.egpBalanceLabel.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        self.dollarBalanceLabel = CTkLabel(self.bordFrame, text=f"DOLLAR: {b1.getDollar()} $",
                                           font=("roboto", 18, "bold"),
                                           text_color="green")
        self.dollarBalanceLabel.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        self.balanceManageLabel = CTkLabel(self.bordFrame, text="Balance management", font=("roboto", 16, "bold"),
                                           width=100,
                                           fg_color="black", corner_radius=15)
        self.balanceManageLabel.grid(row=3, column=0, padx=20, pady=20)

        self.withdrawButton = CTkButton(self.bordFrame, text="Withdraw", font=("roboto", 15, "bold"), width=150,
                                        height=35,
                                        command=self.withdrawUI)
        self.withdrawButton.grid(row=4, column=0, pady=20, padx=20)

        self.depositButton = CTkButton(self.bordFrame, text="Deposit", font=("roboto", 15, "bold"), width=150, height=35
                                       , command=self.depositUI)
        self.depositButton.grid(row=5, column=0, pady=(0, 20), padx=20)

        self.toolsManageLabel = CTkLabel(self.bordFrame, text="Account management", font=("roboto", 16, "bold"),
                                         width=100,
                                         fg_color="black", corner_radius=15)
        self.toolsManageLabel.grid(row=3, column=1, padx=20, pady=20)

        # changePasswordButton = CTkButton(bordFrame, text="Change password", font=("roboto", 15, "bold"), width=150,
        #                                  height=35, fg_color="brown")
        # changePasswordButton.grid(row=4, column=1, pady=20, padx=20)

        self.logoutButton = CTkButton(self.bordFrame, text="Logout", font=("roboto", 15, "bold"), width=150, height=35,
                                      fg_color="red", command=self.board.destroy)
        self.logoutButton.grid(row=5, column=1, pady=(0, 20), padx=20)

    def withdrawUI(self):
        self.withdraw = CTkToplevel(self.board)
        self.withdraw.resizable(False, False)
        self.withdraw.title("Withdraw")
        self.withdraw.geometry(aspectRatio)

        self.withdraw_frame = CTkFrame(self.withdraw)
        self.withdraw_frame.pack(pady=20, padx=10)

        self.withdrawLabel = CTkLabel(self.withdraw_frame, text='Withdraw', font=('Arial', 20, 'bold'), width=400,
                                      height=50,
                                      bg_color="gray", text_color="black")
        self.withdrawLabel.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        self.withdrawvartype = IntVar()
        self.dollarRadioButton = CTkRadioButton(self.withdraw_frame, text="DOLLAR.$", variable=self.withdrawvartype,
                                                value=1,
                                                font=('arial', 10, 'bold'))
        self.dollarRadioButton.grid(row=1, column=1, pady=10)
        self.egyptRadioButton = CTkRadioButton(self.withdraw_frame, text="EGP.LE", variable=self.withdrawvartype,
                                               value=2,
                                               font=('arial', 10, 'bold'))
        self.egyptRadioButton.grid(row=1, column=2, pady=10)

        self.passwordLabel = CTkLabel(self.withdraw_frame, text='Password', font=('Arial', 14, 'bold'))
        self.passwordLabel.grid(row=2, column=0, pady=10, padx=10)
        self.passwordEntery = CTkEntry(self.withdraw_frame, width=300, font=('Arial', 12), show="*")
        self.passwordEntery.grid(row=2, column=1, columnspan=3, pady=10, padx=10)

        self.amountLabel = CTkLabel(self.withdraw_frame, text='Amount', font=('Arial', 14, 'bold'))
        self.amountLabel.grid(row=3, column=0, pady=10, padx=10)
        self.amountEntery = CTkEntry(self.withdraw_frame, width=300, font=('Arial', 12))
        self.amountEntery.grid(row=3, column=1, columnspan=3, pady=10, padx=10)

        self.withdrawButton = CTkButton(self.withdraw_frame, text='Submit', width=300, font=('Arial', 12, 'bold'),
                                        command=self.Withdraw)
        self.withdrawButton.grid(row=4, column=0, columnspan=4, pady=10, padx=10)

        self.backWithdrawButton = CTkButton(self.withdraw_frame, text='Exit', width=200, fg_color="brown",
                                            font=('Arial', 10, 'bold'), command=self.withdraw.destroy)
        self.backWithdrawButton.grid(row=5, column=0, columnspan=4, pady=10, padx=10)

    def depositUI(self):
        self.deposit = CTkToplevel(self.board)
        self.deposit.resizable(False, False)
        self.deposit.title("Deposit")
        self.deposit.geometry(aspectRatio)

        self.deposit_frame = CTkFrame(self.deposit)
        self.deposit_frame.pack(pady=20, padx=20)

        self.depositLabel = CTkLabel(self.deposit_frame, text='Deposit', font=('Arial', 20, 'bold'), width=400,
                                     height=50,
                                     bg_color="gray", text_color="black")
        self.depositLabel.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        self.depositvartype = IntVar()
        self.dollarRadioButton = CTkRadioButton(self.deposit_frame, text="DOLLAR.$", variable=self.depositvartype,
                                                value=1, font=('arial', 10, 'bold'))
        self.dollarRadioButton.grid(row=1, column=1, pady=10)
        self.egyptRadioButton = CTkRadioButton(self.deposit_frame, text="EGP.LE", variable=self.depositvartype, value=2,
                                               font=('arial', 10, 'bold'))
        self.egyptRadioButton.grid(row=1, column=2, pady=10)

        self.amountLabel = CTkLabel(self.deposit_frame, text='Amount', font=('Arial', 14, 'bold'))
        self.amountLabel.grid(row=3, column=0, pady=10, padx=10)
        self.amountEntery = CTkEntry(self.deposit_frame, width=300, font=('Arial', 12))
        self.amountEntery.grid(row=3, column=1, columnspan=3, pady=10, padx=10)

        self.depositButton = CTkButton(self.deposit_frame, text='Submit', width=300, font=('Arial', 12, 'bold'),
                                       command=self.Deposit)
        self.depositButton.grid(row=4, column=0, columnspan=4, pady=10, padx=10)

        self.backButton = CTkButton(self.deposit_frame, text='Exit', width=200, fg_color="brown",
                                    font=('Arial', 10, 'bold'),
                                    command=self.deposit.destroy)
        self.backButton.grid(row=5, column=0, columnspan=4, pady=10, padx=10)

    # ----------------------------------------- END GUI --------------------------------------------------

    def setID(self):
        with open('id history.txt', 'w') as f:
            f.write(f'{self.__id}')
            f.close()

    def getID(self):
        with open('id history.txt', 'r') as f:
            id = f.readline()
            id = id.split('\n')
            self.__id = int(id[0])
            f.close()
            return self.__id

    def setUserID(self, id):
        self.__id = id

    def getUserID(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPassword(self, pwd):
        self.__password = pwd

    def getPassword(self):
        return self.__password

    def setDollar(self, d):
        self.__Dollarbalance = d

    def getDollar(self):
        return self.__Dollarbalance

    def setEgpt(self, egp):
        self.__LEbalance = egp

    def getEgpt(self):
        return self.__LEbalance

    def userLogin(self, id, name, password):
        global b1
        b1 = Bank()
        b1.setUserID(id)
        b1.getData()
        print(id, " ", b1.getUserID(), " - ", name, " ", b1.getName(), password, " ", b1.getPassword())
        if b1.getName() == name and b1.getPassword() == password and b1.getUserID() == id:
            self.dashboard()
            self.ctkmessagbox_showinfo(self.board, "Login success!", "Successfully logged in!")
        else:
            self.ctkmessagbox_showerror(self.login, "Invalid login!", "Data is not valid!!")

    def createAcc(self):
        self.getID()
        name = input('Enter Account Name: ')
        if os.path.exists(f'new acc {self.__id}.txt'):
            print("Choose Another Name And Try Again!")
            self.createAcc()
        elif len(name) < 5:
            print("Name Of Account Must Be Longer Than 5 Digits")
            self.createAcc()
        else:
            password = input('Enter Account Password: ')
            if len(password) < 8:
                print("Password Must Be Larger Than 8 Digits!")
            else:
                self.__userid = self.__id
                self.__name = name
                self.__password = password
                self.writeNewData()
                if os.path.exists(f'new acc {self.__userid}.txt'):
                    print("Do You Want To Deposit?")
                    choice = input("Type (Y) for Yes, any key to cancel: ")
                    # if choice.upper() == 'Y':
                    #     # self.deposit()
                    # else:
                    #     # self.describe('')
        self.__id = int(self.getID()) + 1
        self.setID()

    def deleteAcc(self):
        print("!! Are You Sure To Delete Your Account !!")
        print("-If You Deleted Your Account, Your Dollars And Egypt Balance Will Be '0' !\n")
        print("!! Note: To Cancel Type '!' In Password")
        Pw = input("\nEnter Account Password: ")
        if os.path.exists(f'new acc {self.__userid}.txt'):
            if Pw == self.__password:
                os.remove(f'new acc {self.__userid}.txt')
                print('Account Deleted \n')
            elif Pw == '!':
                print("Delete Account Canceled.\n")
            else:
                print('Wrong Password! \n')
        else:
            print('Failed To Delete Account! \n')

    def changePwd(self):
        old_password = input("Enter Your Old Password: ")
        if os.path.exists(f'new acc {self.__userid}.txt'):
            global db, eb
            with open(f'new acc {self.__userid}.txt', 'r') as f:
                id = f.readline().split('\n')
                self.__userid = str(id[0])
                user = f.readline().split('\n')
                self.__name = str(user[0])
                pwd = f.readline().split('\n')
                pwd = str(pwd[0])
                self.__password = pwd
                db = f.readline().split('\n')
                self.__Dollarbalance = int(db[0])
                eb = f.readline().split('\n')
                self.__LEbalance = int(eb[0])
                f.close()

            if old_password == self.__password:
                # self.describe('normal')
                new_password = input("Enter New Password: ")
                re_new_password = input("Re Enter New Password: ")
                if new_password == self.__password:
                    print("This Password Is Same As Old Password.")
                elif new_password != re_new_password:
                    print("New Password Not Match!")
                    print("\nTry Again ?\nType (Y) For Yes, any key to cancel")
                    sw = input(">> ")
                    if sw.upper() == 'Y':
                        self.changePwd()
                    else:
                        pass
                elif len(new_password) < 8:
                    print("Password Must Be Longer Than 8 Digit!")
                    print("\nTry Again ?\nType (Y) For Yes, any key to cancel")
                    sw = input(">> ")
                    if sw.upper() == 'Y':
                        self.changePwd()
                    else:
                        pass
                else:
                    self.__password = new_password
                    self.writeNewData()
                    print("Password Has Been Changed!")
                    # self.describe('normal')

            else:
                print("Incorrect Password!")
        else:
            print("An Error, Can't Change Password While Now!")

    def getData(self):
        if os.path.exists(f'new acc {b1.getUserID()}.txt'):
            with open(f'new acc {b1.getUserID()}.txt', 'r') as f:
                id = f.readline().split('\n')
                user = f.readline().split('\n')
                pwd = f.readline().split('\n')
                db = f.readline().split('\n')
                eb = f.readline().split('\n')
            f.close()
            b1.setUserID(str(id[0]))
            b1.setName(str(user[0]))
            b1.setPassword(str(pwd[0]))
            b1.setDollar(int(db[0]))
            b1.setEgpt(int(eb[0]))
        else:
            self.ctkmessagbox_showerror(self.login, "Login error!", "There is no account with this data!")

    def writeNewData(self):
        try:
            with open(f'new acc {b1.getUserID()}.txt', 'w') as f:
                f.write(f'{b1.getUserID()}\n')
                f.write(f'{b1.getName()}\n')
                f.write(f'{b1.getPassword()}\n')
                f.write(f'{b1.getDollar()}\n')
                f.write(f'{b1.getEgpt()}\n')
                f.close()
        except:
            self.ctkmessagbox_showerror("", "error!", "There error in this account data!")

    # def describe(self, type):
    #     if os.path.exists(f'new acc {self.__userid}.txt'):
    #         with open(f'new acc {self.__userid}.txt', 'r') as f:
    #             id = f.readline().split('\n')
    #             self.__userid = str(id[0])
    #             user = f.readline().split('\n')
    #             self.__name = str(user[0])
    #             pwd = f.readline().split('\n')
    #             pwd = str(pwd[0])
    #             self.__password = pwd
    #             db = f.readline().split('\n')
    #             self.__Dollarbalance = int(db[0])
    #             eb = f.readline().split('\n')
    #             self.__LEbalance = int(eb[0])
    #         f.close()
    #         if pwd == self.__password:
    #             if type == 'normal':
    #                 print("\nAccount Details")
    #                 print(f"Account ID       '{self.__userid}'\n"
    #                       f"Account Name     '{self.__name}'\n"
    #                       f"Account Password '{self.__password}' \n"
    #                       f"$-Balance=       '{self.__Dollarbalance}' \n"
    #                       f"EGP-Balance=     '{self.__LEbalance}' \n")
    #             else:
    #                 print("\nAccount Details")
    #                 print(f"Account ID       '{self.__userid}'\n"
    #                       f"Account Name     '{self.__name}'\n"
    #                       # f"Account Password '{self.__password}' \n"
    #                       f"$-Balance=       '{self.__Dollarbalance}' \n"
    #                       f"EGP-Balance=     '{self.__LEbalance}' \n")
    #         else:
    #             print("Other Account Use This Name!")
    #     else:
    #         print("No Data To Describe!")

    def Deposit(self):
        if self.depositvartype.get() == 1:
            try:
                Amount = int(self.amountEntery.get())
                if Amount >= 50 and Amount + b1.getDollar() <= 5000000:
                    b1.setDollar(b1.__Dollarbalance + Amount)
                    b1.writeNewData()
                    self.ctkmessagbox_showinfo(self.deposit, "Success!", f"{Amount}$ was deposit.")
                    self.dollarBalanceLabel.configure(text=f"DOLLAR: {b1.getDollar()} $")
                elif Amount > 1000000:
                    self.ctkmessagbox_showerror(self.deposit, "error!", "Can't deposit more than 1000000$")
                else:
                    self.ctkmessagbox_showerror(self.deposit, "error!", "Can't Deposit Balance Less Than 50$")
            except:
                self.ctkmessagbox_showerror(self.deposit, "error!", "Value Must Be Numeric Only!")
        elif self.depositvartype.get() == 2:
            try:
                Amount = int(self.amountEntery.get())
                if Amount >= 100 and Amount + b1.getEgpt() <= 9000000:
                    b1.setEgpt(b1.__LEbalance + Amount)
                    b1.writeNewData()
                    self.ctkmessagbox_showinfo(self.deposit, "Success!", f"{Amount}.LE was deposit.")
                    self.egpBalanceLabel.configure(text=f"EGP: {b1.getEgpt()}.LE")
                elif Amount > 1000000:
                    self.ctkmessagbox_showerror(self.deposit, "error!", "Can't deposit more than 1000000.LE")
                else:
                    self.ctkmessagbox_showerror(self.deposit, "error!", "Can't Deposit Balance Less Than 100.LE")
            except:
                self.ctkmessagbox_showerror(self.deposit, "error!", "Value Must Be Numeric Only!")
        else:
            self.ctkmessagbox_showerror(self.deposit, "error!", "Select stock type!")

    def Withdraw(self):
        if self.passwordEntery.get() == b1.getPassword():
            if self.withdrawvartype.get() == 1:
                try:
                    Amount = int(self.amountEntery.get())
                    if Amount <= b1.getDollar() and Amount >= 50:
                        b1.setDollar(b1.__Dollarbalance - Amount)
                        b1.writeNewData()
                        self.ctkmessagbox_showinfo(self.withdraw, "Success!", f"{Amount}$ was withdrawn.")
                        self.dollarBalanceLabel.configure(text=f"DOLLAR: {b1.getDollar()} $")
                    else:
                        self.ctkmessagbox_showerror(self.withdraw, "error!", "$-Balance Not Enough!!")
                except:
                    self.ctkmessagbox_showerror(self.withdraw, "error!", "Value Must Be Numeric Only!")
            elif self.withdrawvartype.get() == 2:
                try:
                    Amount = int(self.amountEntery.get())
                    if Amount <= b1.getEgpt() and Amount >= 100:
                        b1.setEgpt(b1.__LEbalance - Amount)
                        b1.writeNewData()
                        self.ctkmessagbox_showinfo(self.withdraw, "Success!", f"{Amount}.LE was withdrawn.")
                        self.egpBalanceLabel.configure(text=f"EGP: {b1.getEgpt()}.LE")
                    else:
                        self.ctkmessagbox_showerror(self.withdraw, "error!", "EGP-Balance Not Enough!!")
                except:
                    self.ctkmessagbox_showerror(self.withdraw, "error!", "Value Must Be Numeric Only!")
            else:
                self.ctkmessagbox_showerror(self.withdraw, "error!", "Select stock type")
        else:
            self.ctkmessagbox_showerror(self.withdraw, "error!", "Invalid data!")


Bank().mainMenu()
