class Calculator:                       #creating the calculator class
    def __init__(self, num1,num2):      #initializing the two numbers as the parameters
        self.n1=num1
        self.n2=num2
    def add(self):                      #function to add the two number
        global result
        result=self.n1+self.n2
    def substract(self):                #function to substract the first number with the second
        global result
        result=self.n1-self.n2
    def multiply(self):                 #function to multiply the two numbers with each other
        global result
        result=self.n1*self.n2
    def divide(self):                   #function to divide the first number with the second
        global result
        result=float((self.n1/self.n2))
while True:                             #A whie loop to keep the calculator running while the user hasnt specified to quit
    result=0                            #result variable to store the result(s)

    a=int(input("Enter a number:"))     #the first number input from the user
    #below are instructions on binary operator input(s)
    print("+: add\n-: minus\n*: times\n/: division\nInput 'n' at any time to show result")
    c=input("Enter a binary operator:") #the binary input from the user
    c=c.replace(" ","")                 #this removes any unnecessary spaces
    b=int(input("Enter another number:"))   #the second number input
    x=Calculator(a,b)                      #making x a new calculator class object with a and b as parameters
    while True:

        if c=="+":              #the ifs and elifs are to detect which binary operator were entered by the user
            x.add()
            a=result
        elif c=="-":
            x.substract()
            a=result
        elif c=="*":
            x.multiply()
            a=result
        elif c=="/":
            x.divide()
            a=result
        elif c=="n":        #this is to detect when the user wants the result
            break
        else:
            print("Wrong input!")   #error message should the user mistyped

        c=input("Enter a binary operator:") #the second binary operator input (optional)
        c=c.replace(" ","")
        if c=="n":
            break
        d=input("Enter another number:")   #a number to operate the second binary operator
        if d!="n":                         #this is to detect if the user wants the result already or no
            b=int(d)
        elif d=="n":
            break
        x=Calculator(a,b)               #creating a new object with new inputted parameters
    print(result)                       # printing result
    d=input("Continue?[y/n]:\n")    #this will ask the user whether or not to continue after the result is shown
    if d.lower()=="y":              #restart the loop and do more calculation
        pass
    elif d.lower()=="n":            #end the whole program
        break
