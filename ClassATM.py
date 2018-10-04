accounts=[]
pins=[]                     #all the list will be filled with the account details
balances=[]
initialID=941116            #initialID to give to the accounts
name=""
handle=""                   #initialized variables that will be used later
index=0
recip=""
identifier=""

f=True                      #condition that becomes the indicator to stop for 2 loops
class ATM:                                                          #creation of the class ATM
    def __init__(self,name,initialID,balance,pocketMoney,pin):      #initializing all the parameters or attributes
        self.name=name
        accounts.append(self.name)
        self.id=initialID
        initialID+=1
        self.bal=balance
        balances.append(self.bal)
        self.pockmon=pocketMoney
        self.pin=pin
        pins.append(self.pin)
    def getBalance(self):                                          #function to show balance
       print("Rp.%19d"%(self.bal))
    def getPocket(self):                                           #optional function to show pocketed money
        print("Rp.%19d"%(self.pockmon))
    def withdraw(self,amount):                                      #function to withdraw money
        self.amn=amount
        self.bal-=self.amn
        self.pockmon+=self.amn
    def deposit(self,amount):                                       #function to deposit money
        self.amn2=amount
        self.bal+=self.amn2
    def debit(self,amount):                                         #function to charge debit
        self.amn3=amount
        self.bal-=self.amn3
    def setPin(self,pin):                                           #function to set the account PIN
        self.pin=pin
        pins.append(self.pin)
    def transfer(self,recipient,amount):                            #function to transfer to another account
        global recip
        global identifier
        self.rec=recipient
        self.amn3=amount
        identifier=""
        if recipient in accounts:
            a=accounts.index(recipient)
            balances[a]=balances[a]+self.amn3
            handle.withdraw(self.amn3)
        else:
            print("Recipient not in the system!")

    def showAccDetail(self):                                        #function to show account details
        print("Name   :",self.name,"\nID     :",self.id,"\nBalance:",self.bal)



def makeAcc(name,balance,pocketMoney,pin):                      #function to create an account(new object)
    global handle
    global initialID
    handle=ATM(name,initialID,balance,pocketMoney,pin)
    initialID+=1


while f==True:                                          #one of the loop controlled by f
    logIn=input("Log in or Sign up:\n")                     #option to log in or sign up for a new acc
    if logIn.lower()=="sign up":                                   #procedures to follow to sign up
        name2=input("Input your name first name below:\n")
        name22=input("Input your name last name below:\n")
        name23=name2+" "+name22
        initDeposit=int(input("Enter your initial deposit:\n"))
        while True:                                                 #keeps the loop going until the correct PIN format is inputted
            pinCode=int(input("Enter a 4 digit PIN:\n"))
            if len(str(pinCode))==4:
                break
            else:
                print("Incorrect PIN format!")
        makeAcc(name23,initDeposit,0,pinCode)           #making and showing the details of the acc
        handle.showAccDetail()

    elif logIn.lower()=="log in":
        name3=input("Enter your full name  : ")                 #procedures to follow to log into an acc
        if name3 in accounts:
            index=accounts.index(name3)
            while True:
                password=input("Enter your 4 digit pin: ")      #keep loops going until the correct PIN is entered
                if int(password)==pins[index]:
                    break
                else:
                    print("Wrong password")
        else:
            print("No record in the system")
            break
        while f==True:                                  #the second loop controlled by f
            dep="1) Deposit"
            wit="Withdraw (2"
            deb="3) Debit"                                                  #the option screen
            tra="Transfer (4"
            qt="5) Quit"
            print("          Transactions          ")
            print("================================")
            print("%-20s %10s " % (dep,wit))
            print("%-20s %11s " % (deb,tra))
            print("%-20s" % (qt))
            transaction=input("Enter your transaction type here: ")
            if transaction=="1" or transaction.lower()=="deposit":                      #procedures to deposit money
                while True:
                    transaction2=int(input("How much do you want to deposit?:\n"))
                    if transaction2>=0:
                        handle.deposit(transaction2)
                        print("Your balance is now: ")
                        handle.getBalance()
                        break
                    else:
                        print("Deposit input incorrect!")
            elif transaction=="2" or transaction.lower()=="withdraw":                   #procedures to withdraw money
                while True:
                    transaction2=int(input("How much do you want to withdraw?:\n"))
                    if handle.bal>transaction2:
                        handle.withdraw(transaction2)
                        print("Your balance is now: ")
                        handle.getBalance()
                        break
                    else:
                        print("Insufficient funds!")
            elif transaction=="3" or transaction.lower()=="debit":                       #procedures to charge debit
                while True:
                    transaction2=int(input("How much will you be charged?:\n"))
                    if handle.bal>transaction2:
                        handle.debit(transaction2)
                        print("Your balance is now: ")
                        handle.getBalance()
                        break
                    else:
                        print("Insufficient funds!")
            elif transaction=="4" or transaction=="transfer":               #procedures to transfer to another acc
                while True:
                    for x in accounts:
                        print(x)
                    transaction2=input("Enter the name of the recipient:\n")
                    if transaction2 in accounts:
                        transaction3=int(input("Enter the amount:\n"))
                        handle.transfer(transaction2,transaction3)
                        print("Your balance is currently:\n")
                        handle.getBalance()
                        break
                    else:
                        "Recipient Not Found!"

            elif transaction=="5" or transaction.lower()=="quit":           #exit or make more transaction
                while True:
                    transaction2=input("Are you sure [Yes/No]?\n")
                    if transaction2.lower()=="yes":
                        f=False
                        break
                    elif transaction2.lower()=="no":
                        break




