#floor() ---> it will return the largest less than or equeal to the given number
import math

n=7.6
F_num= math.floor(n)
print(F_num)

#  what is diff between / and //
# / its means division floating number of given number & // it will return internumber
print(5//2)
print(5/2)

# pass function as a aruguments
def add(x,y):
    return x+y
def funct(func,a,b):
    return add(a,b)
print(funct(add,10,10))

#what is lambda function:
#lambda is anonymous function it used to define a function in the single line
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

#what is upper() function:
#its used to convert my string Lower to Higher
s1 ="mathankumar"
s2=lambda func:func.upper()
print(s2(s1))