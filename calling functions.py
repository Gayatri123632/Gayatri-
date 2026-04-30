#without arguments and without return values
def sum():
    a=20
    b=30
    add=a+b
    print(add)
sum()

#with arguments and without return values
def sum(a,b):
    c=a+b
    print(c)
sum(40,40)

#without arguments and with return values
def sum():
    a=30
    b=10
    return a+b
print(sum())

#with arguments and with return values
def sum(a,b):
    c=a+b
    return c
add=sum(20,10)
print(add)

#return statements:
def sum(a,b):
    return a+b
print(sum(10,15))

