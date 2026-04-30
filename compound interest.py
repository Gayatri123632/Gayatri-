p=float(input("enter principle amount"))
r=float(input("enter rate of interest"))
t=float(input("enter time in years"))
amount=p*(1+r/100)**t
ci=amount-p
print("total amount=",amount)
print("compound interest=",ci)
