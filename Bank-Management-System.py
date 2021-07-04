
password = 1234

def Admin():
    print("Enter password")
    user = int(input())
    if user == password:
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
  AccountCount = int(fileAC.read())   #class variable
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
Admin()
AccntCount()
obj.Withdrawl()
obj.Deposit()
obj.CheckBalance()


