day=int(input("enter day number:"))
switch={
    1:"monday",
    2:"tuesday",
    3:"wednesday",
    4:"thursday",
    5:"friday",
    6:"saturday",
    7:"sunday",
    }
print(switch.get(day,"invaild day"))
