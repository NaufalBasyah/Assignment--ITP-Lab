x=int(input("Enter the number of rows:\n (The diamond row will be (2x-1) with x being the input number)\n"))
#Pythagorean Triangle
b=1
for i in range (0,x):
    print("*"*(i+b))
    if i==(x-1):
        print(" ")
#Pythagorean Triangle Reversed
str="*"
for i in range(1,x+1):
    for j in range(i,i+1):
        print (str.rjust(10," "))
        str=str+"*"
    if i==x:
        print(" ")
#Upside down Pythagorean Triangle
for i in range(0,x):
    print("*"*(x-i))
    if i==(x-1):
        print(" ")
#Upside down Pythagorean Triangle Reversed
for i in range(0,x):
    print(" "*(i+1)+"*"*(x-i))
    if i==(x-1):
        print(" ")
#Pyramid Triangle
str="*"
for i in range(1,x+1):
   for j in range(i,i+1):
      print (str.rjust(x+i-1," "))
   str=str+"**"
   if i==x:
        print(" ")
#Diamond
a=1
b=1
for i in range(1,2*x):
    if a<=((2*x)-1):
        print(" "*(x-i)+"*"*a)
        a+=2
    elif a>((2*x)-1):
        print(" "*(i-x)+"*"*(a-4*b))
        a+=2
        b+=1
