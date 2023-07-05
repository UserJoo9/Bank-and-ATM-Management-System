from CTkMessagebox import CTkMessagebox as CTkMsg
from customtkinter import *
from win32api import GetSystemMetrics
from PIL import Image

width = int(GetSystemMetrics(0) / 3)
height = int(GetSystemMetrics(1) / 6)
aspectRatio = f'{width}+{height}'

window_bg = CTkImage(light_image=Image.open("img/e-Banking.jpg"),
                                  dark_image=Image.open("img/e-Banking.jpg"),
                                  size=(800, 600))


class Bank():

    def __init__(self):
        self.__id = "100"
        self.__userid = id
        self.__name = None
        self.__password = None
        self.__Dollarbalance = 0
        self.__LEbalance = 0


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

    # ------------------------------------------- START GUI -----------------------------------------------


    def mainMenu(self):
        self.root = CTk()
        self.root.title("e-Bank")
        self.root.resizable(False, False)
        self.root.geometry(aspectRatio)

        self.bg_label = CTkLabel(self.root, text="", image=window_bg)
        self.bg_label.place(x=0, y=0)

        self.mainFrame = CTkFrame(self.root)
        self.mainFrame.pack(pady=30, padx=30)

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

        self.bg_label = CTkLabel(self.login, text="", image=window_bg)
        self.bg_label.place(x=0, y=0)

        self.loginFrame = CTkFrame(self.login)
        self.loginFrame.pack(pady=30, padx=30)

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
        self.login.after(100, self.login.lift)

    def createAccUI(self):
        self.create = CTkToplevel(self.root)
        self.create.title("Create Account")
        self.create.resizable(False, False)
        self.create.geometry(aspectRatio)

        self.bg_label = CTkLabel(self.create, text="", image=window_bg)
        self.bg_label.place(x=0, y=0)

        self.createFrame = CTkFrame(self.create)
        self.createFrame.pack(pady=30, padx=30)

        self.createLabel = CTkLabel(self.createFrame, text="Create Account", font=("roboto", 22, "bold"), height=50,
                                    width=400)
        self.createLabel.pack(pady=10, padx=20)

        self.createUsernameEntry = CTkEntry(self.createFrame, placeholder_text="Username", width=300)
        self.createUsernameEntry.pack(pady=(0, 10), padx=20)

        self.createPassEntry = CTkEntry(self.createFrame, placeholder_text="Password", width=300,
                                        show="*")
        self.createPassEntry.pack(pady=(0, 10), padx=20)

        self.reCreatePassEntry = CTkEntry(self.createFrame, placeholder_text="Password again", width=300,
                                          show="*")
        self.reCreatePassEntry.pack(pady=(0, 10), padx=20)

        self.createAccButton = CTkButton(self.createFrame, text="Submit", font=("roboto", 18, "bold"), width=300,
                                         height=30, command=self.createAcc)
        self.createAccButton.pack(pady=(0, 10), padx=20)

        self.exitCreateAccButton = CTkButton(self.createFrame, text="Exit", font=("roboto", 15, "bold"), width=200,
                                             height=20,
                                             fg_color="brown", hover_color="red", command=self.create.destroy)
        self.exitCreateAccButton.pack(pady=10, padx=20)
        self.create.after(100, self.create.lift)

    def dashboard(self):
        try:
            self.login.destroy()
        except:
            pass
        self.board = CTkToplevel(self.root)
        self.board.title("Account Details")
        self.board.resizable(False, False)
        self.board.geometry(aspectRatio)

        self.bg_label = CTkLabel(self.board, text="", image=window_bg)
        self.bg_label.place(x=0, y=0)

        self.bordFrame = CTkFrame(self.board)
        self.bordFrame.pack(padx=30, pady=30)

        self.boardLabel = CTkLabel(self.bordFrame, text="Dashboard & Control", font=("roboto", 22, "bold"), width=400,
                                   height=50)
        self.boardLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        self.idLabel = CTkLabel(self.bordFrame, text=f"ID: {self.getUserID()}", font=("roboto", 18, "bold"))
        self.idLabel.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.nameLabel = CTkLabel(self.bordFrame, text=f"NAME: {self.getName()}", font=("roboto", 18, "bold"))
        self.nameLabel.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.egpBalanceLabel = CTkLabel(self.bordFrame, text=f"EGP: {self.getEgpt()}.LE", font=("roboto", 18, "bold"),
                                        text_color="orange")
        self.egpBalanceLabel.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        self.dollarBalanceLabel = CTkLabel(self.bordFrame, text=f"DOLLAR: {self.getDollar()} $",
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

        self.transferButton = CTkButton(self.bordFrame, text="Transfer", font=("roboto", 15, "bold"), width=150, height=35
                                        , command=self.transfer_transactionUI)
        self.transferButton.grid(row=6, column=0, pady=(0, 20), padx=20)

        self.toolsManageLabel = CTkLabel(self.bordFrame, text="Account management", font=("roboto", 16, "bold"),
                                         width=100,
                                         fg_color="black", corner_radius=15)
        self.toolsManageLabel.grid(row=3, column=1, padx=20, pady=20)

        changePasswordButton = CTkButton(self.bordFrame, text="Change password", font=("roboto", 15, "bold"), width=150,
                                         height=35, fg_color="brown", command=self.changePasswordUi)
        changePasswordButton.grid(row=4, column=1, pady=20, padx=20)

        self.logoutButton = CTkButton(self.bordFrame, text="Logout", font=("roboto", 15, "bold"), width=150, height=35,
                                      fg_color="red", command=self.board.destroy)
        self.logoutButton.grid(row=5, column=1, pady=(0, 20), padx=20)

        deleteAccountButton = CTkButton(self.bordFrame, text="Delete Account!", font=("roboto", 12, "bold"), width=100, height=30,
                                      fg_color="red", command=self.deleteAcc)
        deleteAccountButton.grid(row=6, column=1, pady=10)

        # CTkMsg(master=self.board, title="Login success!", message="Successfully logged in!")
        self.board.after(100, self.board.lift)

    def changePasswordUi(self):
        self.changePass = CTkToplevel(self.root)
        self.changePass.resizable(False, False)
        self.changePass.title("Change password")

        self.changePasswordBanner = CTkLabel(self.changePass, text="Change password", font=("roboto", 24, "bold"))
        self.changePasswordBanner.pack(pady=10, padx=10)

        self.newPasswordEntry = CTkEntry(self.changePass, placeholder_text="New password", show="*", width=250)
        self.newPasswordEntry.pack(pady=10, padx=10)

        self.reNewPasswordEntry = CTkEntry(self.changePass, placeholder_text="Re new password", show="*", width=250)
        self.reNewPasswordEntry.pack(pady=10, padx=10)

        self.changePasswordButton = CTkButton(self.changePass, text="OK", width=100, command=self.changePwd)
        self.changePasswordButton.pack(padx=10, pady=5)

        self.changePass.after(100, self.changePass.lift)

    def withdrawUI(self):
        self.withdraw = CTkToplevel(self.board)
        self.withdraw.resizable(False, False)
        self.withdraw.title("Withdraw")
        self.withdraw.geometry(aspectRatio)

        self.bg_label = CTkLabel(self.withdraw, text="", image=window_bg)
        self.bg_label.place(x=0, y=0)

        self.withdraw_frame = CTkFrame(self.withdraw)
        self.withdraw_frame.pack(pady=30, padx=30)

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
        self.withdraw.after(100, self.withdraw.lift)

    def depositUI(self):
        self.deposit = CTkToplevel(self.board)
        self.deposit.resizable(False, False)
        self.deposit.title("Deposit")
        self.deposit.geometry(aspectRatio)

        self.bg_label = CTkLabel(self.deposit, text="", image=window_bg)
        self.bg_label.place(x=0, y=0)

        self.deposit_frame = CTkFrame(self.deposit)
        self.deposit_frame.pack(pady=30, padx=30)

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
        self.deposit.after(100, self.deposit.lift)

    def transfer_transactionUI(self):
        self.trans = CTkToplevel(self.board)
        self.trans.resizable(False, False)
        self.trans.title("Transfer")
        self.trans.geometry(aspectRatio)

        self.frm = CTkFrame(self.trans)
        self.frm.pack(pady=30, padx=30)

        self.transfer_label = CTkLabel(self.frm, text='Transfer', font=('Arial', 20, 'bold'), width=400,
                                     height=50,
                                     bg_color="gray", text_color="black")
        self.transfer_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        self.transtype = IntVar()
        self.dollarTransRadioButton = CTkRadioButton(self.frm, text="DOLLAR.$", variable=self.transtype,
                                                value=1, font=('arial', 10, 'bold'))
        self.dollarTransRadioButton.grid(row=1, column=1, pady=10)
        self.egyptTransRadioButton = CTkRadioButton(self.frm, text="EGP.LE", variable=self.transtype, value=2,
                                               font=('arial', 10, 'bold'))
        self.egyptTransRadioButton.grid(row=1, column=2, pady=10)

        self.idTransLabel = CTkLabel(self.frm, text='Account ID', font=('Arial', 14, 'bold'))
        self.idTransLabel.grid(row=3, column=0, pady=10, padx=10)
        self.idTransEntery = CTkEntry(self.frm, width=300, font=('Arial', 12))
        self.idTransEntery.grid(row=3, column=1, columnspan=3, pady=10, padx=10)

        self.amountTransLabel = CTkLabel(self.frm, text='Amount', font=('Arial', 14, 'bold'))
        self.amountTransLabel.grid(row=4, column=0, pady=10, padx=10)
        self.amountTransEntery = CTkEntry(self.frm, width=300, font=('Arial', 12))
        self.amountTransEntery.grid(row=4, column=1, columnspan=3, pady=10, padx=10)

        self.secretLabel = CTkLabel(self.frm, text='Password', font=('Arial', 14, 'bold'))
        self.secretLabel.grid(row=5, column=0, pady=10, padx=10)
        self.secretTransEntery = CTkEntry(self.frm, width=300, font=('Arial', 12), show="*")
        self.secretTransEntery.grid(row=5, column=1, columnspan=3, pady=10, padx=10)

        self.transButton = CTkButton(self.frm, text='Submit', width=300, font=('Arial', 12, 'bold'),
                                       command=self.Transfer)
        self.transButton.grid(row=6, column=0, columnspan=4, pady=10, padx=10)

        self.trans.after(100, self.trans.lift)


    # ----------------------------------------- END GUI --------------------------------------------------

    def userLogin(self, id, name, password):
        self.setUserID(id)
        self.getData()
        if self.getName() == name and self.getPassword() == password and self.getUserID() == id:
            self.dashboard()
        else:
            CTkMsg(title="Invalid login!", message="Data is not valid!!", icon="cancel")

    def createAcc(self):
        if self.createUsernameEntry.get().startswith(" ") or len(self.createUsernameEntry.get()) < 5:
            CTkMsg(title="Invalid data!", message="Name Of Account Must Be Longer Than 5 Digits", icon="cancel")
        elif len(self.createPassEntry.get()) <= 8:
            CTkMsg(title="Weak password!", message="Create a strong password!", icon="cancel")
        elif self.createPassEntry.get() != self.reCreatePassEntry.get():
            CTkMsg(title="Invalid data!", message="Passwords must be similar!", icon="cancel")
        else:
            self.setUserID(int(self.getID()) + 1)
            self.setName(self.createUsernameEntry.get())
            self.setPassword(self.createPassEntry.get())
            self.setEgpt(0)
            self.setDollar(0)
            self.writeNewData()
            self.userLogin(str(self.getUserID()), self.getName(), self.getPassword())
            self.setID()
            self.create.destroy()

    def deleteAcc(self):
        if CTkMsg(title="!! Are You Sure To Delete Your Account !!",
               message="if You Deleted Your Account, Your Dollars And Egypt Balance Will Be '0' !",
                  option_1="Yes", option_2="No", icon="warning").get() == "Yes":
            Pw = CTkInputDialog(title="Verification!", text="Password required!").get_input()
            if Pw == self.getPassword():
                if os.path.exists(f'new acc {self.getUserID()}.txt'):
                    self.board.destroy()
                    os.remove(f'new acc {self.getUserID()}.txt')
                    CTkMsg(title="Notify", message='Account Deleted.')
                else:
                    CTkMsg(title="Error!", message='Failed To Delete Account!', icon="cancel")
            else:
                CTkMsg(title="Error!", message='Wrong Password!', icon="cancel")

    def changePwd(self):
        if len(self.newPasswordEntry.get()) <= 8:
            CTkMsg(title="Weak password!", message="Create a strong password!", icon="cancel")
        elif self.newPasswordEntry.get() != self.reNewPasswordEntry.get():
            CTkMsg(title="Invalid data!", message="Passwords must be similar!", icon="cancel")
        else:
            if os.path.exists(f'new acc {self.__userid}.txt'):
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
                    self.setPassword(self.newPasswordEntry.get)
                    self.writeNewData()
                    CTkMsg(title="Password changed!", message="Password changed successfully!")


    def getData(self):
        if os.path.exists(f'new acc {self.getUserID()}.txt'):
            with open(f'new acc {self.getUserID()}.txt', 'r') as f:
                id = f.readline().split('\n')
                user = f.readline().split('\n')
                pwd = f.readline().split('\n')
                db = f.readline().split('\n')
                eb = f.readline().split('\n')
            f.close()
            self.setUserID(str(id[0]))
            self.setName(str(user[0]))
            self.setPassword(str(pwd[0]))
            self.setDollar(int(db[0]))
            self.setEgpt(int(eb[0]))


    def writeNewData(self):
        try:
            with open(f'new acc {self.getUserID()}.txt', 'w') as f:
                f.write(f'{self.getUserID()}\n')
                f.write(f'{self.getName()}\n')
                f.write(f'{self.getPassword()}\n')
                f.write(f'{self.getDollar()}\n')
                f.write(f'{self.getEgpt()}\n')
                f.close()
        except:
            CTkMsg(title="error!", message="There error in this account data!", icon="cancel")

    def Deposit(self):
        if self.depositvartype.get() == 1:
            try:
                Amount = int(self.amountEntery.get())
                if Amount >= 50 and Amount + self.getDollar() <= 5000000:
                    self.setDollar(self.__Dollarbalance + Amount)
                    self.writeNewData()
                    CTkMsg(master=self.deposit, title="Success!", message=f"{Amount}$ was deposit.")
                    self.dollarBalanceLabel.configure(text=f"DOLLAR: {self.getDollar()} $")
                elif Amount > 1000000:
                    CTkMsg(master=self.deposit, title="error!",
                           message="Can't deposit more than 1000000$", icon="cancel")
                else:
                    CTkMsg(master=self.deposit, title="error!",
                           message="Can't Deposit Balance Less Than 50$", icon="cancel")
            except:
                CTkMsg(master=self.deposit, title="error!", message="Value Must Be Numeric Only!", icon="cancel")
        elif self.depositvartype.get() == 2:
            try:
                Amount = int(self.amountEntery.get())
                if Amount >= 100 and Amount + self.getEgpt() <= 9000000:
                    self.setEgpt(self.__LEbalance + Amount)
                    self.writeNewData()
                    CTkMsg(master=self.deposit, title="Success!", message=f"{Amount}.LE was deposit.")
                    self.egpBalanceLabel.configure(text=f"EGP: {self.getEgpt()}.LE")
                elif Amount > 1000000:
                    CTkMsg(master=self.deposit, title="error!",
                           message="Can't deposit more than 1000000.LE", icon="cancel")
                else:
                    CTkMsg(master=self.deposit, title="error!",
                           message="Can't Deposit Balance Less Than 100.LE", icon="cancel")
            except:
                CTkMsg(master=self.deposit, title="error!", message="Value Must Be Numeric Only!", icon="cancel")
        else:
            CTkMsg(master=self.deposit, title="error!", message="Select stock type!", icon="cancel")

    def Withdraw(self):
        if self.passwordEntery.get() == self.getPassword():
            if self.withdrawvartype.get() == 1:
                try:
                    Amount = int(self.amountEntery.get())
                    if self.getDollar() >= Amount >= 50:
                        self.setDollar(self.__Dollarbalance - Amount)
                        self.writeNewData()
                        CTkMsg(master=self.withdraw, title="Success!", message=f"{Amount}$ was withdrawn.")
                        self.dollarBalanceLabel.configure(text=f"DOLLAR: {self.getDollar()} $")
                    else:
                        CTkMsg(master=self.withdraw, title="error!", icon="cancel", message="$-Balance Not Enough!!")
                except:
                    CTkMsg(master=self.withdraw, title="error!", icon="cancel", message="Value Must Be Numeric Only!")
            elif self.withdrawvartype.get() == 2:
                try:
                    Amount = int(self.amountEntery.get())
                    if self.getEgpt() >= Amount >= 100:
                        self.setEgpt(self.__LEbalance - Amount)
                        self.writeNewData()
                        CTkMsg(master=self.withdraw, title="Success!", message=f"{Amount}.LE was withdrawn.")
                        self.egpBalanceLabel.configure(text=f"EGP: {self.getEgpt()}.LE")
                    else:
                        CTkMsg(master=self.withdraw, title="error!", icon="cancel", message="EGP-Balance Not Enough!!")
                except:
                    CTkMsg(master=self.withdraw, title="error!", icon="cancel", message="Value Must Be Numeric Only!")
            else:
                CTkMsg(master=self.withdraw, title="error!", icon="cancel", message="Select stock type")
        else:
            CTkMsg(master=self.withdraw, title="error!", icon="cancel", message="Invalid data!")

    def Transfer(self):
        if self.secretTransEntery.get() == self.getPassword():
            destAcc = f"new acc {self.idTransEntery.get()}.txt"
            if self.transtype.get() == 1:
                try:
                    if os.path.exists(destAcc):
                        Amount = int(self.amountTransEntery.get())
                        if self.getDollar() >= Amount >= 10:
                            self.setDollar(self.__Dollarbalance - Amount)
                            self.writeNewData()
                            with open(destAcc, 'r') as f:
                                id = f.readline().split('\n')[0]
                                user = f.readline().split('\n')[0]
                                pwd = f.readline().split('\n')[0]
                                db = f.readline().split('\n')[0]
                                eb = f.readline().split('\n')[0]
                            f.close()
                            db = int(db) + Amount
                            with open(destAcc, 'w') as f:
                                f.write(f'{id}\n')
                                f.write(f'{user}\n')
                                f.write(f'{pwd}\n')
                                f.write(f'{db}\n')
                                f.write(f'{eb}\n')
                                f.close()
                            CTkMsg(master=self.trans, title="Success!", message=f"{Amount}$ was transferred to account ({id}).")
                            self.dollarBalanceLabel.configure(text=f"DOLLAR: {self.getDollar()} $")
                        else:
                            CTkMsg(master=self.trans, title="error!", icon="cancel", message="$-Balance Not Enough!!")
                        self.secretTransEntery.delete("0", "end")
                        self.idTransEntery.delete("0", "end")
                        self.amountTransEntery.delete("0", "end")
                    else:
                        CTkMsg(master=self.trans, title="error!", icon="cancel", message="There is now account with this id!")
                except:
                    CTkMsg(master=self.trans, title="error!", icon="cancel", message="Value Must Be Numeric Only!")
            elif self.transtype.get() == 2:
                try:
                    if os.path.exists(destAcc):
                        Amount = int(self.amountTransEntery.get())
                        if self.getEgpt() >= Amount >= 50:
                            self.setEgpt(self.__LEbalance - Amount)
                            self.writeNewData()
                            with open(destAcc, 'r') as f:
                                id = f.readline().split('\n')[0]
                                user = f.readline().split('\n')[0]
                                pwd = f.readline().split('\n')[0]
                                db = f.readline().split('\n')[0]
                                eb = f.readline().split('\n')[0]
                            f.close()
                            eb = int(eb) + Amount
                            with open(destAcc, 'w') as f:
                                f.write(f'{id}\n')
                                f.write(f'{user}\n')
                                f.write(f'{pwd}\n')
                                f.write(f'{db}\n')
                                f.write(f'{eb}\n')
                                f.close()
                            CTkMsg(master=self.trans, title="Success!", message=f"{Amount}.LE was transferred to account ({id}).")
                            self.dollarBalanceLabel.configure(text=f"EGP: {self.getEgpt()}.LE")
                        else:
                            CTkMsg(master=self.trans, title="error!", icon="cancel", message="LE Balance Not Enough!!")
                        self.secretTransEntery.delete("0", "end")
                        self.idTransEntery.delete("0", "end")
                        self.amountTransEntery.delete("0", "end")
                    else:
                        CTkMsg(master=self.trans, title="error!", icon="cancel", message="There is now account with this id!")
                except:
                    CTkMsg(master=self.trans, title="error!", icon="cancel", message="Value Must Be Numeric Only!")
        else:
            CTkMsg(master=self.trans, title="error!", icon="cancel", message="Wrong password!!")

if __name__ == "__main__":
    Bank().mainMenu()
