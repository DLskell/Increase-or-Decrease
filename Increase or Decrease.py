#generally useful for sales, but also for other uses, it can be used to increase or decrease a given amount by a pre-determined percentage
a=3
while a!=1 and a!=2 and a!=0:
    print("Type 1 for an increase\nType 2 for a decrease\nType 0 to cancel")
    a=int(input("Type here : "))

if a==1:
    b=float(input("The data to increase : "))
    c=float(input("The percentage increase : "))
    b=b+b*c/100
    print("The result is : ",b)

if a==2:
    b=float(input("The data to reduce : "))
    c=float(input("The reduction percentage : "))
    b=b-(b*c/100)
    print("The result is : ",b)
