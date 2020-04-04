from array import *
#val = array('i',[1,2,3,4,5])

# #If we want to copy the array into new array. If square is not needed then keep only a instead of a*a
# newArray = array(val.typecode,(a*a for a in val))
# print(newArray)
# # If need to print the values in new lines
# for i in newArray:
#     print(i)

# val.reverse()
# print(val)

# # one way when we dont know the range, gets the index values like val[0].
# for i in range(len(val)):
#     print(val[i])

# # Other way when we dont know the range. It gets the values directly.
# for i in val:
#     print(i)

# # one way when we know the range, gets the index values like val[0].
# for i in range(5):
#     print(val[i])

#If we need to take values from user to create an array.

arr = array('i',[])
n = int(input("Please Enter the length of an array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)