# https://www.programiz.com/python-programming/args-and-kwargs

#Normal function
def add(x,y,z):
    sum=x+y+z
    return sum

print(add(1,2,3))

#with *args
def add(*args): #args can be of any name. These arguments makes tuple.
    print(type(args))
    sum=0
    for i in args:
        sum= sum+i
    return sum
print(add(1,2,3))


#keyword arguments..eg: Violeta=5.5, Marco=6.5, Paola=8
#with *kwargs(keyworded)-- Python passes variable length non keyword argument to function using *args but we cannot use this to pass keyworded argument. For this problem Python has got a solution called **kwargs, it allows us to pass the variable length of keyword arguments to the function.
#In the function, we use the double asterisk ** before the parameter name to denote this type of argument. The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as the parameter excluding double asterisk **.
def add(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,v)
add(first=1,second=2)

# import pandas as pd

i = 10
j = 10.0
k = 8+3+j
print(type(i),type(j),type(k))
print(i,j,k)

