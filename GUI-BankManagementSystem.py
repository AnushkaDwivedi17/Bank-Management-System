from tkinter import *
from tkinter import messagebox

password = 1234
global checkp

def Admin():
    root = Tk()
    root.title("Bank")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#33A5FF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Admin", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    
    lb1 = Label(labelFrame,text="Password: ", bg='black', fg='blue')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    checkp = Entry(labelFrame)
    checkp.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black')
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black')
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    
    root.mainloop()
def CheckP():
    if checkp == password:
         print("Displaying All user's Information")
         fileAdmin = open('Admin','r')
         print(fileAdmin.read())
         fileAdmin.close()
    return

def AccntCount():
    file = open("Account-Count")
    print("Total Accounts in Bank are: ", file.read())
    file.close()
    return

class Bank:
  fileAC = open('Account-Count','r')
  AccountCount = int(fileAC.read())
  fileAC.close()
  
  def __init__(self, name):
 
    self.name = name
    try:
         file = open(name,'x')
         file.write(str(0))
         file.close()

         fileAC = open('Account-Count','w')
         fileAC.write(str(Bank.AccountCount+1))
         fileAC.close()

         Bank.AccountCount += 1
         fileAdmin = open('Admin','a')
         mail = input("Enter your mail id: ")
         fileAdmin.write(str(Bank.AccountCount)+"\n"+name+"\n"+mail+"\n")
         fileAdmin.close()
    
         
    except FileExistsError:
        print("Welcome Back")
  
  def CheckBalance(self):
    file = open(self.name)
    balance = int(file.read())
    file.close()
    print("Your Balance is: " , balance)

  def Withdrawl(self):
    print("Enter the amount you want to withdraw: ")
    amount = int(input())
    file = open(self.name)
    balance = int(file.read())
    file.close()
    balance = balance - amount
    print("Remaining Balance:", balance)
    file = open(self.name,'w')
    file.write(str(balance))
    file.close()

  def Deposit(self):
    print("Enter the amount you want to deposit: ")
    amount = int(input())
    file = open(self.name)
    balance = int(file.read())
    file.close()
    balance = balance + amount
    print("Remaining Balance:", balance)
    file = open(self.name,'w')
    file.write(str(balance))
    file.close()


     
obj = Bank('Anushka')
##Admin()
##AccntCount()
##obj.Withdrawl()
##obj.Deposit()
##obj.CheckBalance()





root = Tk()
root.title("Bank Management System")
root.minsize(width=400,height=400)
root.geometry("600x500")
Canvas1 = Canvas(root) 
Canvas1.config(bg="#12a4d9")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#33A5FF",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \nBank Management System", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Admin",bg='black', fg='blue', command=Admin)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Account Count",bg='black', fg='blue', command=AccntCount)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Withdraw Money",bg='black', fg='blue', command=obj.Withdrawl)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Deposit Money",bg='black', fg='blue', command = obj.Deposit)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
   
btn5 = Button(root,text="Check Balance",bg='black', fg='blue', command = obj.CheckBalance)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
root.mainloop()
