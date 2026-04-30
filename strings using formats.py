Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name="gayatri"
>>> age=18
>>> print(f"my name is{name}and i am {age}years old")
my name isgayatriand i am 18years old
>>> print("my name is {} and i'm {} years old".format(name,age))
my name is gayatri and i'm 18 years old
>>> print("my name is {0} and i'm {1} years old".format(name,age))
my name is gayatri and i'm 18 years old
>>> print("my name is {n} and i'm {a} years old".format(n=name,a=age))
my name is gayatri and i'm 18 years old
>>> print("my name is %s and i'm %d years old".%(name,age))
SyntaxError: invalid syntax
>>> print("my name is %s and i'm %d years old"%(name,age))
my name is gayatri and i'm 18 years old
