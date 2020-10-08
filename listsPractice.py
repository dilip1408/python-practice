# # union of two lists
# mylist1 = [1,2,3,4,5]
# mylist2 = [4,5,6,7,8]
#
# def union(mylist1,mylist2):
#     return set(mylist1+mylist2)
#
# if __name__ == "__main__":
#     print("In main")
# print(union(mylist1,mylist2))
#
# set1 = {2, 4, 5, 6}
# set2 = {4, 6, 7, 8}
# set3 = {4, 6, 8}
#
# # union of two sets
# print("set1 intersection set2 : ", set1.intersection(set2))
#
# # union of three sets
# print("set1 intersection set2 intersection set3 :", set1.intersection(set2, set3))

######sum of integers in list############
# l = [2,2,1]

# def sum_int(integers):
#     k = 0
#     for i in integers:
#         k = k+i
#     return k
# print("---",sum_int(l))
###with list  comprehension, It will not work. A list comprehension produces a list that is just as long as its input. You will need one of Python's other functional tools (specifically reduce() in this case) to fold the sequence into a single value.
#https://stackoverflow.com/questions/16632124/how-to-emulate-sum-using-a-list-comprehension
# k=0
# x = [k := k + i for i in [2,2,1]] #This will not work
# print(x)

# #This works only from v3.8. #Starting Python 3.8, and the introduction of assignment expressions (PEP 572) (:= operator), we can use and increment a variable within a list comprehension and thus reduce a list to the sum of its elements:
# total = 0
# [total := total + x for x in [1, 2, 3, 4, 5]] #with assignment expression
######

#########program to multiplies all the individual items in a list####
list# x = [2,3,6] # expected [4, 9, 36]
# ## x = 2,3,6 #This is valid and type is tuple
# z=[]
# def multiples(input):
#     for i in x:
#        j= i*i
#        z.append(j)
#     return z
# print("Multiples of given list",multiples(x))
# #using list comprehension
# z = [i*i for i in x]
# print(z)

#########program to multiplies all the items in a list(one value * next value)####
# x = [2,3,4]
# tot = 1
# for i in x:
#     tot = tot * i
# print(tot)
##comprehension will not work, see above

##########Python program to get the largest number from a list.###
##one way is to use max(x) function
##second way is to apply x.sort() and take the last element. and take the last element x[-1] or slcing - x[-1:]
# x = [8,2,5,9,3,-1]
# def largest_number(input):
#     y = 0
#     for i in input:
#         if i > y:
#             y=i
#     return y
# print(largest_number(x))
###########program to get the smallest number from a list####
##one way is to use min(x) function
##second way is to apply x.sort() and take the last element. and take the last element x[0] or slcing - list1[:1]
# x = [8,2,5,9,3,-1]
# def smallest_num(input):
#     z = input[0]
#     for i in input:
#         if i < z:
#             z=i
#     return z
#
# print("Smallest number",smallest_num(x))

#############Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.#####
#one way
# list1 = ['abc','xyz','xyx','1221']
# # i=0
# def same_character(input):
#     di = {}
#     i=0
#     for s in range(len(list1)):
#         if len(list1[s]) > 2:
#             element = list1[s]
#             first_character = element[0]
#             last_character = element[-1]
#             if first_character == last_character:
#                 i += 1
#                 di[i]=list1[s]
#     return (di)
#
# print(same_character(list1))
#
# #other way
# for l in list1:
#     if len(l)> 2 and l[0] == l[-1]:
#         print(l)
###########
#########Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples####
# t_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# def last(n):
#     return n[-1]
# def sorted_list_last(tuples):
#     return sorted(tuples, key=last)
# print(sorted_list_last(t_list))

# d = {'name':'Dilip','age':30}
#
# for i in range(len(d)):
#     print(d[i])

# lists basics - Add/modify/remove/
#creating an empty list
# l = []
# print("Empty list",l)
# l.append([1,2,3])
# l.append(4)
# l.extend([5,6,7,7,8])
# print(l)
# j = l.remove(7)
# print(l,j)
# print(len(l))
# l1 = [1,2,3,4,5,6,7,8]
# l_copy = l.copy()
# print(l_copy)
# l_copy.remove(8)
# print(l_copy)
# print(l)
# l_copy[0] = 1
# print(l_copy)
# print(l_copy.pop())
# l_copy.insert(0,9)
# print(l_copy)
# l.append([1,2,3])
# print(l)

l2 = [1,2,3,'a','b','e','c']
print(l2.pop(1))

l2.reverse()
print(l2)

