#How to access characters in string by index ?
string = 'Dilip'
# print(string[0])

#Python strings are immutable, therefore we can not change content of string using [] operator. If we try to modify the string with [] then it will return error
#TypeError: 'str' object does not support item assignment
# string[0] = 'v'
# print(string)

for e in range(len(string)-1,-1,-1):
    print(string[e])