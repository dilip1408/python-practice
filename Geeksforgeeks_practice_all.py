#Add two numbers
# a,b = 1,2
# print(a+b)
#
# #By default input comes as string.
# fn = int(input("First Number"))
# sn = int(input("Second number:"))
# print(fn+sn)

#######
# Factorial

# x = 5
# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f * i
#     return f
# result = fact(x)
# print(result)

#Factorial using recursion(Calling a function from itself)
# By definition,((!)factorial) 1! is 1 and 0! is 1.
# x = 4
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
# result = fact(x)
# print(result)

# import sys
# sys.setrecursionlimit(10)
# def greet():
#     print("Hello")
#     greet()
#
# greet()

# def factorial(n):
#     # single line to find factorial
#     return 1
#     if (n == 1):
#     else
#         n * factorial(n - 1);
# # Driver Code
# num = 5;
# print(factorial(num))

# input = 94701
#
# input_s = str(input)
# for i in input_s:
#     print("|",end='')
#     print("*" * int(i))

# # extracting the dictionary to keys and values seperately and converting the 2 lists to dictionary
# dictionary = {1:'One', 2:'Two', 3:'Three'}
# print((dictionary))
# k =[]
# v=[]
# for i,j in dictionary.items():
#     k.append(i)
#     v.append(j)ope
#
# print("keys::",k)
# print("Values::",v)
#
# #One way to convert 2 lists to dict 'e'
# e = {k[i]:v[i] for i in range(len(k))}
# print(e)
# #Other way to convert 2 lists to dict 'd'
# d = dict(zip(k,v))
# print(d)

#3rd way to convert 2 lists to dict 'dicti'
# dicti = {i:j for i,j in zip(k,v)}
# print(dicti)


###########################
#zip,unzip
# name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]
# marks = [40, 50, 60, 70]
#
# # using zip() to map values
# mapped = zip(name, roll_no, marks)
# m = set(mapped)
# print(m)
#
# #Unzipping the values
# n,r,m = list(zip(*m))
# print(n,r,m)

#prime number check for a specified value
num = 7
if (num > 1):
    for i in range(2, num):
        if (num % i == 0):
            print("From IF condition: i value ==> ", i, "and num is => ", num)

        else:
            print("i value ==> ", i, " and num is => ", num)
            print(num," is a prime number")




# # Print all prime numbers in an interval
# start = 11
# end= 25
# for val in range(start,end+1):
#     if (val>1):
#         for n in range(2,val):
#             if(val%n)==0:
#                 break
#         else:
#             print(val)

# x = None
# y = None
# print(x == y)
# print(type(x))
# #To know memory location of a variable
# print(id(x))

# ##break,pass,continue condition####3
# from builtins import range
#
# text = "Dilip"
# for i in text:
#     # print(i)
#     if(i == "i" or i=="l"):
#         break
#     else:
#         print("in if-else block--Break has been triggered, cursor not been through if condition")
# print("Out of the loop")
#
# i=0
# while True:
#     if text[i] == 'i' or  text[i] == 'l':
#         break
#     i=i+1
#     print(i)
# print("out of loop")

# for i in text:
#     # print(i)
#     if(i == "i" or i=="l" or i=='p'):
#         pass
#     else:
#         print("in if-else block only when the if condition is not True")
# print("Out of the loop")

# for i in text:
#     # print(i)
#     if(i == "i" or i=="l" or i=='p'):
#         continue
#     else:
#         print("in if-else block-")
# print("Out of the loop")

# ##break,pass condition####3

#Negative loop#
# for i in range(20,10,-2):
#     print(i)
#Negative loop#

# l = [2,7,1,8,11,7,7,6,7,10,7]
# l = list(set(l))
# l.remove(7)
# print(l)

# l1 = [2,7,1,8,11,7,7,6,7,10,7]
# l1 = dict.fromkeys(l1)
# l1.pop(7)
# print(l1)

# def f(a):
# 	return a
# a='a'
# print(type(f(a)))
# print(type(3.5+5))
# a = [1,2,3,None,(),[],]open
# for i in a:
#     print(i)
#
#
# for line in reversed(list(open('C:/Users/dvoruga/Documents/Python scripts/filename.txt'))):
#     print(line.rstrip())

