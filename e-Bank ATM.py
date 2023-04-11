# ------------------------------------ APIs ----------------------------------------#

import os
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk


# --------------------------------- Describe -------------------------------------#

def describeUi(*args):
    global describeLabel, idLabel, idEntery, userLabel, userEntery, passwordLabel, passwordEntery, describeeButton, backDescrbeButton
    backFromMainMenu()
    describeLabel = ctk.CTkLabel(top, text='Describe', font=('Arial', 20, 'bold'), width=400, height=50,
                                 bg_color="gray", text_color="black")
    describeLabel.pack()

    idLabel = ctk.CTkLabel(top, text='Account ID', font=('Arial', 14, 'bold'))
    idLabel.pack(pady=10)
    idEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), show="#", corner_radius=15)
    idEntery.pack()

    userLabel = ctk.CTkLabel(top, text='Account Name', font=('Arial', 14, 'bold'))
    userLabel.pack(pady=10)
    userEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), show="$", corner_radius=15)
    userEntery.pack()

    passwordLabel = ctk.CTkLabel(top, text='Account Password', font=('Arial', 14, 'bold'))
    passwordLabel.pack(pady=10)
    passwordEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), show="*", corner_radius=15)
    passwordEntery.pack()

    describeeButton = ctk.CTkButton(top, text='Submit', width=300, font=('Arial', 12, 'bold'),
                             command=describe, corner_radius=15)
    describeeButton.pack(pady=10)

    backDescrbeButton = ctk.CTkButton(top, text='Back', width=200, fg_color="brown", font=('Arial', 12, 'bold'),
                               command=backFromDescribe, corner_radius=15)
    backDescrbeButton.pack(pady=10)

    passwordEntery.bind('<Return>', describe)
    describeeButton.bind('<Return>', describe)
    passwordEntery.bind('<Escape>', backFromDescribe)
    idEntery.bind('<Escape>', backFromDescribe)
    userEntery.bind('<Escape>', backFromDescribe)


def describe(*args):
    id = idEntery.get()
    user = userEntery.get()
    password = passwordEntery.get()
    if os.path.exists(f"new acc {id}.txt"):
        with open(f"new acc {id}.txt", 'r') as f:
            xid = f.readline().split('\n')
            xid = xid[0]
            xuser = f.readline().split('\n')
            xuser = xuser[0]
            xpwd = f.readline().split('\n')
            xpwd = xpwd[0]
            xdollar = f.readline().split('\n')
            xdollar = xdollar[0]
            xegp = f.readline().split('\n')
            xegp = xegp[0]
            if id == xid and user == xuser and password == xpwd:
                messagebox.showinfo("Account Description!", f"Dollar balance: {xdollar}\nEgypt balance: {xegp}")
                idEntery.delete('0', 'end')
                userEntery.delete('0', 'end')
                passwordEntery.delete('0', 'end')
            else:
                messagebox.showerror("Account Error", "Invalid Account Data!")
    else:
        messagebox.showwarning("Account Warning", "Account Not Fount Data!")


def backFromDescribe(*args):
    backDescrbeButton.destroy()
    describeeButton.destroy()
    passwordEntery.destroy()
    passwordLabel.destroy()
    userEntery.destroy()
    userLabel.destroy()
    idEntery.destroy()
    idLabel.destroy()
    describeLabel.destroy()
    MainMenu()


# --------------------------------- Deposit -------------------------------------#

def depositUi(*args):
    global depositLabel, idLabel, idEntery, userLabel, userEntery, amountLabel, amountEntery, depositButton, backButton, dollarRadioButton, egyptRadioButton, var
    backFromMainMenu()
    depositLabel = ctk.CTkLabel(top, text='Deposit', font=('Arial', 20, 'bold'), width=400, height=50,
                                bg_color="gray", text_color="black")
    depositLabel.pack()

    var = IntVar()
    dollarRadioButton = ctk.CTkRadioButton(top, text="DOLLAR.$", variable=var, value=1, font=('arial', 10, 'bold'))
    dollarRadioButton.place(x=100, y=80)
    egyptRadioButton = ctk.CTkRadioButton(top, text="EGP.LE", variable=var, value=2, font=('arial', 10, 'bold'))
    egyptRadioButton.place(x=230, y=80)

    idLabel = ctk.CTkLabel(top, text='Account ID', font=('Arial', 14, 'bold'))
    idLabel.pack(pady=(60, 10))
    idEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), corner_radius=15)
    idEntery.pack()

    amountLabel = ctk.CTkLabel(top, text='Amount', font=('Arial', 14, 'bold'))
    amountLabel.pack(pady=10)
    amountEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), corner_radius=15)
    amountEntery.pack()

    depositButton = ctk.CTkButton(top, text='Submit', width=300, font=('Arial', 12, 'bold'), command=deposit,
                                  corner_radius=15)
    depositButton.pack(pady=10)

    backButton = ctk.CTkButton(top, text='Back', width=200, fg_color="brown", font=('Arial', 10, 'bold'),
                               command=backFromDeposit, corner_radius=15)
    backButton.pack(pady=10)


def deposit(*args):
    global amount, id
    id = idEntery.get()
    if var.get() == 1:
        try:
            amount = int(amountEntery.get())
            if os.path.exists(f"new acc {id}.txt"):
                with open(f"new acc {id}.txt", 'r') as f:
                    xid = f.readline().split('\n')
                    xid = xid[0]
                    xuser = f.readline().split('\n')
                    xuser = xuser[0]
                    xpwd = f.readline().split('\n')
                    xpwd = xpwd[0]
                    xdollar = f.readline().split('\n')
                    xdollar = int(xdollar[0])
                    xegp = f.readline().split('\n')
                    xegp = xegp[0]

                    if amount > 50 or amount < 10000:
                        with open(f"new acc {id}.txt", 'w') as f:
                            f.write(f'{xid}\n')
                            f.write(f'{xuser}\n')
                            f.write(f'{xpwd}\n')
                            f.write(f'{xdollar + amount}\n')
                            f.write(f'{xegp}\n')
                            f.close()
                        simpleDescripe()
                    else:
                        messagebox.showwarning("Amount Alert!",
                                               "Can't Deposit Less Than 50.$ and Larger Than 10,000.$")
            else:
                messagebox.showwarning("Account Warning", "Account Not Fount Data!")
        except:
            messagebox.showerror("Value Error", "Amount Must be Numeric Only!")

    elif var.get() == 2:
        try:
            amount = int(amountEntery.get())
            if os.path.exists(f"new acc {id}.txt"):
                with open(f"new acc {id}.txt", 'r') as f:
                    xid = f.readline().split('\n')
                    xid = xid[0]
                    xuser = f.readline().split('\n')
                    xuser = xuser[0]
                    xpwd = f.readline().split('\n')
                    xpwd = xpwd[0]
                    xdollar = f.readline().split('\n')
                    xdollar = xdollar[0]
                    xegp = f.readline().split('\n')
                    xegp = int(xegp[0])

                    if amount > 100 or amount < 50000:
                        with open(f"new acc {id}.txt", 'w') as f:
                            f.write(f'{xid}\n')
                            f.write(f'{xuser}\n')
                            f.write(f'{xpwd}\n')
                            f.write(f'{xdollar}\n')
                            f.write(f'{xegp + amount}\n')
                            f.close()
                        simpleDescripe()
                    else:
                        messagebox.showwarning("Amount Alert!",
                                               "Can't Deposit Less Than 100.EGP and Larger That 50,000.EGP")

            else:
                messagebox.showwarning("Account Warning", "Account Not Fount Data!")
        except:
            messagebox.showerror("Value Error", "Amount Must be Numeric Only!")
    else:
        messagebox.showerror('Unknown Stock', "Pleas Select Stock Type!")


def simpleDescripe():
    with open(f"new acc {id}.txt", 'r') as f:
        xid = f.readline().split('\n')
        xid = xid[0]
        xuser = f.readline().split('\n')
        xuser = xuser[0]
        xpwd = f.readline().split('\n')
        xpwd = xpwd[0]
        xdollar = f.readline().split('\n')
        xdollar = xdollar[0]
        xegp = f.readline().split('\n')
        xegp = xegp[0]
        if var.get() == 1:
            messagebox.showinfo("Account Description!", f"Deposited {amount}.$")
        elif var.get() == 2:
            messagebox.showinfo("Account Description!", f"Deposited {amount}.EGP")
        else:
            messagebox.showerror("Error", "An Error!")


def backFromDeposit(*args):
    backButton.destroy()
    depositButton.destroy()
    amountEntery.destroy()
    amountLabel.destroy()
    idEntery.destroy()
    idLabel.destroy()
    egyptRadioButton.destroy()
    dollarRadioButton.destroy()
    depositLabel.destroy()
    MainMenu()


# ---------------------------------- Withdraw -----------------------------------#

def withdrawUI(*args):
    global withdrawLabel, idLabel, idEntery, userLabel, userEntery, passwordLabel, passwordEntery, amountLabel, amountEntery, withdrawButton, backWithdrawButton, dollarRadioButton, egyptRadioButton, var
    backFromMainMenu()
    withdrawLabel = ctk.CTkLabel(top, text='Withdraw', font=('Arial', 20, 'bold'), width=400, height=50,
                                 bg_color="gray", text_color="black")
    withdrawLabel.pack()

    var = IntVar()
    dollarRadioButton = ctk.CTkRadioButton(top, text="DOLLAR.$", variable=var, value=1, font=('arial', 10, 'bold'))
    dollarRadioButton.place(x=100, y=80)
    egyptRadioButton = ctk.CTkRadioButton(top, text="EGP.LE", variable=var, value=2, font=('arial', 10, 'bold'))
    egyptRadioButton.place(x=230, y=80)

    idLabel = ctk.CTkLabel(top, text='Account ID', font=('Arial', 14, 'bold'))
    idLabel.pack(pady=(60,10))
    idEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), show="#", corner_radius=15)
    idEntery.pack()

    userLabel = ctk.CTkLabel(top, text='Account Name', font=('Arial', 14, 'bold'))
    userLabel.pack(pady=10)
    userEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), show="$", corner_radius=15)
    userEntery.pack()

    passwordLabel = ctk.CTkLabel(top, text='Account Password', font=('Arial', 14, 'bold'))
    passwordLabel.pack(pady=10)
    passwordEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), show="*", corner_radius=15)
    passwordEntery.pack()

    amountLabel = ctk.CTkLabel(top, text='Amount', font=('Arial', 14, 'bold'))
    amountLabel.pack(pady=10)
    amountEntery = ctk.CTkEntry(top, width=300, font=('Arial', 12), corner_radius=15)
    amountEntery.pack()

    withdrawButton = ctk.CTkButton(top, text='Submit', width=300, font=('Arial', 12, 'bold'), command=withdraw,
                                   corner_radius=15)
    withdrawButton.pack(pady=10)

    backWithdrawButton = ctk.CTkButton(top, text='Back', width=200, fg_color="brown", corner_radius=15,
                                font=('Arial', 10, 'bold'), command=backFromWithdraw)
    backWithdrawButton.pack(pady=10)


def withdraw(*args):
    global amount, id
    id = idEntery.get()
    user = userEntery.get()
    pwd = passwordEntery.get()
    if var.get() == 1:
        try:
            amount = int(amountEntery.get())
            if os.path.exists(f"new acc {id}.txt"):
                with open(f"new acc {id}.txt", 'r') as f:
                    xid = f.readline().split('\n')
                    xid = xid[0]
                    xuser = f.readline().split('\n')
                    xuser = xuser[0]
                    xpwd = f.readline().split('\n')
                    xpwd = xpwd[0]
                    xdollar = f.readline().split('\n')
                    xdollar = int(xdollar[0])
                    xegp = f.readline().split('\n')
                    xegp = xegp[0]

                    if id == xid and user == xuser and pwd == xpwd:
                        if amount < 50 or amount > 10000:
                            messagebox.showwarning("Amount Alert!",
                                                   "Can't Withdraw Less Than 50.$ and Larger Than 10,000.$")
                        elif xdollar < amount:
                            messagebox.showwarning("Amount Alert!", "Account Balance not Enough!")
                        else:
                            nxdollar = xdollar - amount
                            with open(f"new acc {id}.txt", 'w') as f:
                                f.write(f'{xid}\n')
                                f.write(f'{xuser}\n')
                                f.write(f'{xpwd}\n')
                                f.write(f'{nxdollar}\n')
                                f.write(f'{xegp}\n')
                                f.close()
                            withdrawSimpleDescripe()
                            idEntery.delete('0', 'end')
                            userEntery.delete('0', 'end')
                            passwordEntery.delete('0', 'end')
                            amountEntery.delete('0', 'end')
                    else:
                        messagebox.showerror("Account Error", "Invalid Account Data!")
            else:
                messagebox.showwarning("Account Warning", "Account Not Fount Data!")
        except:
            messagebox.showerror("Value Error", "Amount Must be Numeric Only!")

    elif var.get() == 2:
        try:
            amount = int(amountEntery.get())
            if os.path.exists(f"new acc {id}.txt"):
                with open(f"new acc {id}.txt", 'r') as f:
                    xid = f.readline().split('\n')
                    xid = xid[0]
                    xuser = f.readline().split('\n')
                    xuser = xuser[0]
                    xpwd = f.readline().split('\n')
                    xpwd = xpwd[0]
                    xdollar = f.readline().split('\n')
                    xdollar = xdollar[0]
                    xegp = f.readline().split('\n')
                    xegp = int(xegp[0])

                    if id == xid and user == xuser and pwd == xpwd:
                        if amount < 50 or amount > 10000:
                            messagebox.showwarning("Amount Alert!",
                                                   "Can't Withdraw Less Than 50.$ and Larger Than 10,000.$")
                        elif xegp < amount:
                            messagebox.showwarning("Amount Alert!", "Account Balance not Enough!")
                        else:
                            nxegp = xegp - amount
                            with open(f"new acc {id}.txt", 'w') as f:
                                f.write(f'{xid}\n')
                                f.write(f'{xuser}\n')
                                f.write(f'{xpwd}\n')
                                f.write(f'{xdollar}\n')
                                f.write(f'{nxegp}\n')
                                f.close()
                            withdrawSimpleDescripe()
                            idEntery.delete('0', 'end')
                            userEntery.delete('0', 'end')
                            passwordEntery.delete('0', 'end')
                            amountEntery.delete('0', 'end')
                    else:
                        messagebox.showerror("Account Error", "Invalid Account Data!")
            else:
                messagebox.showwarning("Account Warning", "Account Not Fount Data!")
        except:
            messagebox.showerror("Value Error", "Amount Must be Numeric Only!")
    else:
        messagebox.showerror('Unknown Stock', "Pleas Select Stock Type!")


def withdrawSimpleDescripe():
    with open(f"new acc {id}.txt", 'r') as f:
        xid = f.readline().split('\n')
        xid = xid[0]
        xuser = f.readline().split('\n')
        xuser = xuser[0]
        xpwd = f.readline().split('\n')
        xpwd = xpwd[0]
        xdollar = f.readline().split('\n')
        xdollar = xdollar[0]
        xegp = f.readline().split('\n')
        xegp = xegp[0]
        if var.get() == 1:
            messagebox.showinfo("Account Description!", f"Withdrew {amount}.$\nDollar Balance: {xdollar}")
        elif var.get() == 2:
            messagebox.showinfo("Account Description!", f"Withdrew {amount}.EGP\nEgypt Balance: {xegp}")
        else:
            messagebox.showerror("Error", "An Error!")


def backFromWithdraw():
    backWithdrawButton.destroy()
    withdrawButton.destroy()
    amountEntery.destroy()
    amountLabel.destroy()
    passwordEntery.destroy()
    passwordLabel.destroy()
    userEntery.destroy()
    userLabel.destroy()
    idEntery.destroy()
    idLabel.destroy()
    egyptRadioButton.destroy()
    dollarRadioButton.destroy()
    withdrawLabel.destroy()
    MainMenu()


# ---------------------------------- MainMenu ----------------------------------#

def MainMenu():
    global MenuLabel, describeeButton, withdrawButton, depositButton, exiT, frame1
    frame1 = ctk.CTkFrame(top, corner_radius=15)
    frame1.pack(pady=10, padx=10)

    MenuLabel = ctk.CTkLabel(frame1, text='e-Bank ATM', font=('Arial', 20, 'bold'), bg_color="gray", text_color="black",
                             width=400, height=50)
    MenuLabel.pack()
    describeeButton = ctk.CTkButton(frame1, text='Describe', font=('Arial', 18, 'bold'), width=300, height=50,
                             command=describeUi, corner_radius=15)
    describeeButton.pack(pady=30)
    withdrawButton = ctk.CTkButton(frame1, text='Withdraw', font=('Arial', 18, 'bold'), width=300, height=50,
                            command=withdrawUI, corner_radius=15)
    withdrawButton.pack()
    depositButton = ctk.CTkButton(frame1, text='Deposit', font=('Arial', 18, 'bold'), width=300, height=50,
                            command=depositUi, corner_radius=15)
    depositButton.pack(pady=30)
    exiT = ctk.CTkButton(frame1, text='Exit', font=('Arial', 18, 'bold'), fg_color="brown", width=200, command=exit,
                         corner_radius=15, height=30)
    exiT.pack(pady=40)


def backFromMainMenu():
    frame1.destroy()
    MenuLabel.destroy()
    describeeButton.destroy()
    withdrawButton.destroy()
    depositButton.destroy()
    exiT.destroy()


def exit(*args):
    top.destroy()


# ----------------------------------- __home__ ------------------------------------#

top = ctk.CTk()
top.title('e-Bank ATM')
top.resizable(False, False)

MainMenu()

top.mainloop()
