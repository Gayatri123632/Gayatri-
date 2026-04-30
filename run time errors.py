#File not found error
try:
    f=open("student registration")
except:
    print("The file not found")
finally:
    print("Code executed")


#type error
try:
    a="10"
    b=20
    print(a+b)
except:
    print("not vaild")
finally:
    print("The code executed")


#zero division error
try:
    a=12
    b=0
    print(a/b)
except:
    print("not vaild")
finally:
    print("code runs")

#name error
try:
    print(x)
except:
    print("not vaild")
finally:
    print("code runs")

#value error
try:
    a=int("Gayatri")
except:
    print("not vaild")
finally:
    print("code runs")


#key error
try:
    dict={'a':"gayatri",'b':"lucky",'c':"taruni",'d':"lahari"}
    print(dict['f'])
except:
    print("not vaild")
finally:
    print("code runs")


#index error
try:
    list=[1,2,3,4,5]
    print(list[8])
except:
    print("not vaild")
finally:
    print("code runs")


#attribute errors





    


    

