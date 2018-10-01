
ones=("","one","two","three","four","five","six","seven","eight","nine") #tupple of standard numbers from 1-9
tens=("ten","twenty","thrity","fourty","fifty","sixty","seventy","eighty","ninety") #tupple for the tens i.e. 10,20,30,until 90
excep=("eleven","twelve","thriteen") #tupple for numbers that have unique structure( dont follow the norm of ones+teen)

x=int(input("Enter a 1-3 digit number:\n")) #input for the 1-3 digit numbers
y=str(x)                                    #making the number a string in order to manipulate the index
if len(y)==3:                               #if the number is 3 digits
    print(ones[int(y[0])],"hundred",end=" and ")
    if y[1:3]=="11":
        print(excep[0])                 #to detect the exception of 11,22,13 and print it according to the excep tupple
    elif y[1:3]=="12":
        print(excep[1])
    elif y[1:3]=="13":
        print(excep[2])
    elif int(y[1:3])<20 and int(y[1:3])>10:     #if the last 2 digits is in the "teen"s (11-19)
        print(int(y[len(y)-1]),end="")          #to print the last 2 digit with the format lastnumber+teen
        print("teen")
    elif int(y[1:3])<10:                        #if the middle digit is 0
        print(ones[int(y[len(y)-1])])           #print the last number acccording to the ones tupple
    else:
        print(tens[int(y[1])-1],ones[int(y[2])])
elif len(y)==2:                             #if the number is 2 digits
    if y[0:2]=="11":
        print(excep[0])                     #the 11,12,13 will follow the same format as it would for 3 digits above
    elif y[0:2]=="12":
        print(excep[1])
    elif y[0:2]=="13":
        print(excep[2])
    elif int(y[0:2])<20 and int(y[0:2])>10: #the number 14-99 will also follow the same format as it would in 3 digits above
        print(int(y[len(y)-1]),end="")
        print("teen")
    elif int(y[0:2])<10:
        print(ones[int(y[len(y)-1])])
    else:
        print(tens[int(y[0])-1],ones[int(y[1])])
elif len(y)==1:                            #if the number is 1 digit
    if x==0:                               #if input is "0"  it will print "Zero"
        print("Zero")
    else:
        print(ones[x])                         #will print the number according to the ones tupple
