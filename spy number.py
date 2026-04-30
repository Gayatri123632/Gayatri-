n=int(input("enter a number:"))
sumdigits=0
productdigits=0
temp=n
while temp>0:
    digit=temp%10
    sumdigits+=digit
    productdigits*=digit
    temp=temp//10
    if sumdigits ==productdigits:
        print("spy number")
    else:
        print("not a spy number")
