from tkinter import *
password = "1234"       #Password for Admin

def main(): 
    root = Tk()
    app = window1(root)

class window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry("1350x750")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.btnadmin = Button(self.frame,text = "Admin Login", command = self.admin_window)
        self.btnadmin.grid(row = 0, column = 0)

        self.btnuser = Button(self.frame,text = "User Login", command = self.user_window)
        self.btnuser.grid(row = 0, column = 1)

        self.btnuser = Button(self.frame,text = "Account Count", command = self.ac_window)
        self.btnuser.grid(row = 0, column = 3)

    def admin_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window2(self.newWindow)

    def user_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window3(self.newWindow)

    def ac_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window4(self.newWindow)

class window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Admin Login")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        def checkp():
            inp = inputtxt.get(1.0, "end-1c")
            if inp == password:
                fileAdmin = open('Admin','r')
                lbl.config(text = "All user's information: "+fileAdmin.read())
                fileAdmin.close()
            
  
        inputtxt = Text(self.frame,height = 5,width = 20)
  
        inputtxt.pack()
  
        printButton = Button(self.frame,text = "Submit", command = checkp)
        printButton.pack()  

        lbl = Label(self.frame, text = "")
        lbl.pack()
        

class window3:
    def __init__(self,master):
        self.master = master
        self.master.title("User Login and SignUp")
        self.master.geometry("600x500")
        self.frame = Frame(self.master)
        self.frame.pack()

        def creatingobject():
            name = inputtxt.get(1.0, "end-1c")
            fileAC = open('Account-Count','r')
            AccountCount = int(fileAC.read())   
            fileAC.close()
            try:
                 file = open(name,'x')
                 file.write(str(0))
                 file.close()

                 fileAC = open('Account-Count','w')
                 fileAC.write(str(AccountCount+1))
                 fileAC.close()

                 AccountCount += 1
                 fileAdmin = open('Admin','a')
                 fileAdmin.write(str(AccountCount)+"\n"+name+"\n")
                 fileAdmin.close()
    
            except FileExistsError:
               headingFrame1 = Frame(self.master,bg="#33A5FF",bd=5)
##                headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
##                headingLabel = Label(headingFrame1, text="Welcome-Back", bg='black', fg='white', font = ('Courier',15))
##                headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            def checkb():
                headingFrame1 = Frame(self.master,bg="#33A5FF",bd=5)
                headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
                headingLabel = Label(headingFrame1, text="Welcome-Back", bg='black', fg='white', font = ('Courier',15))
                headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
                
            def deposit():
                headingFrame1 = Frame(self.master,bg="#33A5FF",bd=5)
                headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
                headingLabel = Label(headingFrame1, text="Welcome-Back", bg='black', fg='white', font = ('Courier',15))
                headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
                
            def withdraw():
                headingFrame1 = Frame(self.master,bg="#33A5FF",bd=5)
                headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
                headingLabel = Label(headingFrame1, text="Welcome-Back", bg='black', fg='white', font = ('Courier',15))
                headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

                
            self.btn1 = Button(self.frame,text = "Check Balance",padx = 50, command = checkb)
            self.btn1.place(relx=0.2,rely=0.9, relwidth=0.7,relheight=0.9)

            self.btn2 = Button(self.frame,text = "Deposit Money", command = deposit)
            self.btn2.place(relx=600,rely=500, relwidth=0.45,relheight=0.1)

            self.btn3 = Button(self.frame,text = "Withdraw Money", command = withdraw)
            self.btn3.place(relx=0.700,rely=400, relwidth=0.45,relheight=0.1)
        
        inputtxt = Text(self.frame,height = 5,width = 20)
  
        inputtxt.pack()
  
        printButton = Button(self.frame,text = "Submit", command = creatingobject)
        printButton.pack()  

        lbl = Label(self.frame, text = "")
        lbl.pack()

class window4:
    def __init__(self,master):
        self.master = master
        self.master.title("Account-Count")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        def Accntcount():
            file = open('Account-Count','r')
            lbl.config(text = "Account Count: "+file.read())
            file.close()
            
        printButton = Button(self.frame,text = "Check Account Count", command = Accntcount)
        printButton.pack()  

        lbl = Label(self.frame, text = "")
        lbl.pack()
if __name__ == '__main__':
    main()
