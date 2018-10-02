k=True
while k==True:
    a=int(input("Enter a number:"))
    print("+: add\n-: minus\n*: times\n/: division\npow2: to the power of 2\n")
    c=input("Enter a binary operator:")
    c=c.replace(" ","")
    b=input("Enter another number:")
    result=0
    d2=0
    b2=int(b)
    plus=lambda a,b:a+b
    minus=lambda a,b:a-b
    times=lambda a,b:a*b
    divis=lambda a,b:float(a/b)
    pow=lambda a:a**2
    pow2=lambda a,b:a**b





    while True:


        if c=="+":
            a=plus(a,b2)


        elif c=="pow2":
            a=pow(a)

        elif c=="-":
            a=minus(a,b2)


        elif c=="*":
            a=times(a,b2)


        elif c=="/":
            a=divis(a,b2)

        elif c=="n":
            break

        else:
            print("Wrong input!")
        c=input("Enter a binary operator:")
        c=c.replace(" ","")
        if c=="n":
            break
        d=input("Enter another number:")

        if d!="n":
            b2=int(d)
            b=d

        elif d=="n":
            break

    print(a)

    d=input("Continue?[y/n]:\n")
    if d.lower()=="y":
        k=True
    elif d.lower()=="n":
        k=False
