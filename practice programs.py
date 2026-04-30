#iambda to add numbers
add=lambda a,b:a+b
print(add(3,5))
#lambda to find square
square=lambda x:x*x
print(square(5))
#lambda to find cube
cube=lambda x:x*x*x
print(cube(5))
#to check even or odd
even_odd=lambda x:"EVEN" if x%2==0 else "0DD"
print(even_odd(7))
#Write a lambda function to find the maximum of two numbers.
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))
#Use lambda with map() to add 5 to each element in a list.
lst = [1, 2, 3, 4]
result = list(map(lambda x: x + 5, lst))
print(result)
#Use lambda with map() to multiply corresponding elements of two lists.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
result = list(map(lambda x, y: x * y, l1, l2))
print(result)
#Use lambda with filter() to extract even numbers from a list.
list=[1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x%2==0,list)))


