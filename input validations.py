age=input("enter age")
if age.isdigit():
    age=int(age)
    print("vaild age")
else:
        print("invaild age")
        
n=int(input("enter a number"))
if 1<n<10:
    print("vaild")
else:
        print("invaild")

p=input("enter password")
if len(p)>=6:
    print("strong")
else:
        print("too weak")
email=input("enter mail")
if'@'in email and '.'in email:
    print("vaild mail")
else:
              print("invaild mail")
              
        
