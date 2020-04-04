## String reverse
# str = "I am Dilip"
# reversed_str = ''.join(reversed(str))
# print(reversed_str)
# # for i in reversed_str:
# #     print(i)
# rev = str[::-1]
# print(rev)


# index = len(str)
# print(type(index))
# rev_str =[]
# while index > 0:
#     rev_str += str[index-1]
#     index = index - 1

# def reverse(str):
#     s =""
#     for i in str:
#         s = i+s
#     return s
#
# str = "I am Dilip"
# # reverse(str)
# print("The reversed string(using loops) is : ",reverse(str))

# Reverse string using slicing
# string = 'Dilip'
# def rev(string):
#     string = string[::-1]
#     return string
#
# print(rev(string))

vals = [1,2,3,4,6]
# print([x*2 for x in vals if x%2])

#This is equivalent to above list comprehension
for x in vals:
    if(x%2==1):
        print(x*2)

# a = 5
# b = 0
# a,b=b,a
# print(a,b)

# a = ("apple", "banana", "cherry")
# print(type(a))

# #count-pairs-with-given-sum
# arr = [0,10,20,30,40,50,60]
# n = len(arr)
# sum = 10
# count = 0
# for i in range(0,n):
#     print("This is i ----",i)
#     for j in range(i+1,n):
#         if(arr[i] + arr[j]) == sum:
#             print("This is J---", j)
#             print(arr[i],arr[j],"And Sum is",sum)
#             count += 1
# print("matching count", count)
# import numpy as arr
# x = arr.array[(3, 6, 9, 12)]
# print((x))
# -----------------
# #code
# A = [1, 2, 4, 5, 7]
# B = [5, 6, 3, 4, 8]
# lengthA = len(A)
# lengthB = len(B)
# sum = 7
# count = 0
# def sumpairs():
#     global count
#     for i in range(0, lengthA):
#         for j in range(i+1, lengthA):
#             if(A[i] + A[j] == sum):
#                 count += 1
#
#     for i in range(0,lengthB):
#         for j in range(i+1, lengthA):
#             if(B[i] + B[j] == sum):
#                 count += 1
#     return count
#
#
# print(sumpairs())

# --------------
# stringA = "Hi Hi welcome"
# wordtofind = "H"
# wordtofind1 = "i"
# count = 0
# count1 = 0
# dicttostore ={}
# print(type(dicttostore))

# a = stringA.find(wordtofind)
# print(a)
# b = stringA.find(wordtofind,0,10)
# print("This is B value",b)
# if (stringA.find(wordtofind) != -1):
#     for i in iter(stringA):
#         count += 1
#         print(count)
#         key = wordtofind
#         dicttostore[key] = count
#
# print(dicttostore)

# occ = stringA.count(wordtofind)
# print(occ)
##----------------------------
# class my_dictionary(dict):
#
#     # __init__ function
#     def __init__(self):
#         self = dict()
#
#         # Function to add key:value
#
#     def add(self, key, value):
#         self[key] = value
#
#     # Main Function
#
#
# dict_obj = my_dictionary()
#
# dict_obj.add(1, 'Geeks')
# dict_obj.add(2, 'forGeeks')
#
# print(dict_obj)
# ------------------

# str = "Apple Mango Orange Mango Guava Guava Mango"
# list1 = str.split()
# print(list1)
# list2 = []

# import json, pandas as pd
#
# with open('yarnApplications_12hrs.json') as f:
#     data = json.load(f)
# df = pd.DataFrame.from_dict(data, orient='index')
# df.transpose()
# # df = pd.read_json('yarnApplications_12hrs.json')
#
# print((df))

# #-----No. of occurance of a character in a string
# print(str)
# dict1 = {}
# dict2 = {1:'Dilip',2:'Voruganti'}
# str = str.lower()
#
# a = dict2.keys()
# print(a)
# for i in str:
#     if(i in dict1.keys()):
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print(dict1)
#
# dict3 ={}
# for keys in str:
#     dict3[keys] = dict3.get(keys, 0) + 1
# print(dict3)
#
#
# from collections import Counter
# count = Counter(str)
# print(count)
#
# test_str = "GeeksforGeeks"
#
# # using dict.get() to get count
# # of each element in string
# res = {}
#
# for keys in test_str:
#     print(keys)
#     res[keys] = res.get(keys, 0) + 1
#
# # printing result
# print(res)
#


# #Reverse string
# st = "I am Dilip"
# rev_st = ''.join(reversed(st))
# print(st,rev_st)
# str = st[::-1]
# print(str)
# ts=""
# for i in st:
#     print(ts,i)
#     ts = i+ts
# print(ts)

# #convert string to Dict
# string = "key1=value1;key2=value2;key3=value3"
# # dictionary = dict(x.split("=") for x in str.split(";"))
# # print(dictionary)
#
# for x in string.split(";"):
#     print(x)
#     print(x.split("="))

# str = "key1=value1;key2=value2;key3=value3"

# d = dict(x.split("=") for x in str.split(";"))
#
# for k, v in d.items():
#     print(k, v)