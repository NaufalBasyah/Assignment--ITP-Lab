import datetime                     #datetime is imported to show the current date of check-in
single=[0,0,0,0,0,0,0,0,0,0]
full=[1,1,1,1,1,1,1,1,1,1]
double=[0,0,0,0,0,0,0,0,0,0]        #the three containers will be indication of the Single Suites, Double Suites, and Full suites indicator
customers=[]
ds=[]                               #the three containers will be filled with customer objects, room objects and names
names=[]

class Customer:                     #making the customer class
    check_in=0
    length_stay=0                   #the initialised customer attributes (name, age, check in and out time, room number and type as well)
    age=0
    name=""
    roomnum=0
    roomtype=None
    global customers                #the global containers that customer will use
    global names


    def __init__(self):
        self.__a= Customer.age                              #initialising the object with hidden name and age attributes
        self.__n=Customer.name
        Customer.check_in=datetime.date.today()             #setting the check-in date
        customers.append(self)                              #after it's initialised the object will be stored in a container customers
    def setname(self,name):                                 #method to set the private name variable
        Customer.name=name
        names.append(name)                                  #the name is also will be stored in a container, called names
    def setage(self,age):                                   #method to set the private age variable
        Customer.age=age
class SingleSuite(Customer):                    #creating the Single Suite class as a subclass of Customer
    global ds                                   #global ds container that will be used is called
    rate=200,000                                #room rate for the Single Suite
    def __init__(self,Customer):                #creating the object with a customer object inside it
        self.customer=Customer
        self.startDate=super().check_in         #as the vacant room object is made it will stored the check in date in the Customer object
        ds.append(self)                         #storing the vacant room object into a container called ds

    def setCheckOut(self,num):                  #method for the room to be checked-out of and saving the length of stay in the Customer object
        self.customer.length_stay=num
    def calcCost(self,ind):                                             #final step of the check-out to erase from the vacant list and payment
        cost=self.customer.length_stay*SingleSuite.rate[0]*1000
        ds.pop(ind)
        customers.pop(ind)                                              #these will delete the booking info from the lists(room obj, name,customer obj)
        names.pop(ind)
        return cost

class DoubleSuite(Customer):                   #creating the Double Suite class
    global ds                                  #global container ds that will be used is called
    rate=450,000                               #room rate for the Double Suite
    def __init__(self,Customer):
        self.customer=Customer
        self.startDate=super().check_in        #behave about the same way as the init for Single Suite
        ds.append(self)
    def setCheckOut(self,num):
        self.customer.length_stay=num
    def calcCost(self,ind):                         #the check-out and calcCost method also behaves the same way as the Single with different rate for the cost
        cost= self.customer.length_stay*DoubleSuite.rate[0]*1000
        ds.pop(ind)
        customers.pop(ind)
        names.pop(ind)
        return cost
while True:                                     #while loop for the whole UI
    print("Good Day! Welcome to Dick's Halfway Inn!")   #Welcome text
    print("========================================")
    check=input("Check-in or Check-out:\n")             #asking the user for type of check (in or out)
    if check.lower()=="check-in":                       #if the input is check-in
        print("For legal purposes children under 18 aren't allowed to stay in the hotel without a legal guardian")
        print("Please enter your name and age below")
        name=input("\nEnter your full name here:\n")            #name and age input
        age=int(input("Enter your age here:\n"))
        if age>=18:                                     #if the age in 18 and above
            cust=Customer()                             #a Customer object is created and name and age are set
            cust.setname(name)
            cust.setage(age)
            while True:                                 #while loop for the room pick
                print("1.Single Suite (Rp.200,000/nigt\n2.Double Suite (Rp.450,000/night)") #room options
                room=input("Please Pick your room type:")
                if room.lower()=="single suite" or room =="1":                      #if the user picks the Single Suite
                    if single==full:
                        print("All of the Single Suites are currently occupied")    #the message that will show if all Single Suites are booked
                    else:
                        print("")
                        for i in range(0,10):                                       #the check-in process if there is a Single Suite available
                            if single[i]==0:
                                print("Single Suite",str(i+1),"is available!")
                        roompick=input("Enter your prefered room number:\n")
                        cust.roomnum=int(roompick)
                        cust.roomtype='s'
                        single[int(roompick)-1]=1
                        handle=SingleSuite(cust)
                        print("\nYou checked in",cust.check_in,"\n\n")
                        break                                                       #the room pick loop will be broken

                if room.lower()=="double suite" or room =="2":                      #if the user picks Double Suite
                    if double==full:
                            print("All of the Double Suites are currently occupied")   #the message that will show if all Double Suites are booked
                    else:
                        print("")
                        for i in range(0,10):
                            if double[i]==0:
                                print("Double Suite",str(i+1),"is available!")          #the check-in process if there is a Double Suite available
                        roompick=input("Enter your prefered room number:\n")
                        cust.roomnum=int(roompick)
                        cust.roomtype='d'
                        double[int(roompick)-1]=1
                        handle=DoubleSuite(cust)
                        print("\nYou checked in",cust.check_in,"\n\n")
                        break                                                       #the room pick loop will be broken
        else:
            print("Sorry you are not old enough to check in alone")                 #the message will show if the age of the customer is under 18
    elif check.lower()=="check-out":                                      #if the input is check-out
        for x in names:                                                   #printing all the names of checked-in customers
            print(x)
        print("")
        while True:                                                         #while loop for the check-out process
            name=input("Enter your name:\n")
            if name in names:                                                           #checking if the name is stored in the checked-in list
                ind=names.index(name)
                length=int(input("Enter how many days you stayed in the Inn:\n"))
                ds[ind].setCheckOut(length)                        #this will checked out the customer and give them the bill
                if customers[ind].roomtype=="s":
                    single[customers[ind].roomnum-1]=0              #this will change the room status from vacant to available
                elif customers[ind].roomtype=="d":
                    double[customers[ind].roomnum-1]=0
                print("Your bill is Rp.",ds[ind].calcCost(ind))
                print("Thank you and we look forward to your next stay!")

                break                                                       #breaking the check-out loop
            else:
                print("You're name has not be registered")                  #message if name is not registered the loop will start over for the check-out
    elif check.lower()=="quit":
        break                                                               #the message 'quit' will stop the whole program
