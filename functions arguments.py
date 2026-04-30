#required arguments:the number of arguments are present in the function call should be equal to the number of arguments in the function definition
def sum(a,b):
    c=a+b
    print(c)
sum(10,20)
#default arguments: default values are the values it can take the values from the function definition
def sum(x=10,y=20,z=30):
    add=x+y+z
    print(add)
sum(x=10,y=90,z=20)
sum(x=10)
#keyword arguments:keyword arguments are the arguments it can identified by the caller of the function.No:of arguments can be taken in any order
def sum(x,y=30,z=40):
    addition=x+y+z
    print(addition)
sum(10,50,100)
sum(190)
#variable-length arguments(arbitary argumrnts):A variable-length argument allows a function to accept any number of arguments instead of a fixed number.
def display(*no):
    print(no)
display(10,20,40)
#positional arguments:based on the position it will be executed
def greet(name="hello",age=24):
    print(f"my name is {name} and I'm {age} years old")
greet("hello",24)
greet(24,"hello")


    
