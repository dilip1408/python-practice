import pandas as pd
# student = {'name': 'Dilip', 'age': 30, 'courses': ['python','spark','hadoop','java']}
# #student['phone'] = '999999999'
# print(type(student.get('phone','Not found'))) # If the key is not available in dict then customized error message will be displayed.
# # offer[['OFR_ID','l3w_ratio']]
# print(student['courses'])

# if('spark' in student['courses']):
#     print("Spark")

# print(len(student))

# df = pd.DataFrame.from_dict(student)
# print(df)

# for i,e in student.items():
#     print(i,e)

# # Creating a Dictionary -----------------
# # with Integer Keys
# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print("Dictionary with the use of Integer Keys: ")
# print(Dict.items())
#
# # Creating a Dictionary
# # with Mixed keys
# Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
# print("Dictionary with the use of Mixed Keys: ")
# print(Dict)
#
# # Creating a Dictionary
# # with dict() method
# Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# print("\nDictionary with the use of dict(): ")
# print(Dict)
#
# # Creating a Dictionary
# # with each item as a Pair
# Dict = dict([(1, 'Geeks'), (2, 'For')])
# print("\nDictionary with each item as a pair: ")
# print(type(Dict))

# # Initial Dictionary
# Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
#         'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
#         'B': {1: 'Geeks', 2: 'Life'}}
# print("Initial Dictionary: ")
# print(Dict)
#
# # Deleting a Key value
# del Dict[6]
# print("\nDeleting a specific key: ")
# print(Dict)
#
# # Deleting a Key from
# # Nested Dictionary
# del Dict['A'][2]
# print("\nDeleting a key from Nested Dictionary: ")
# print(Dict)
#
# # Deleting a Key
# # using pop()
# a = Dict.pop(5) #Pop will return the removed value of the respective key
# print(a)
# print("\nPopping specific element: ")
# print(Dict)
#
# b = Dict.popitem() #pop item will remove the last key-value pair and returns key-value pair of removed item as tuple
# print(b)
# print(Dict)
#
# Dict.popitem()
# print(Dict)

seq = {'a','b','c'}
lis1 = [1,2]
tup = ((1),(3))


res_seq = (dict.fromkeys(seq,1))
print(res_seq)

ll = tuple(dict.fromkeys(seq))
print(ll)

res_dict = dict.fromkeys(seq, lis1)
print(res_dict)
lis1.append(4)
print(res_dict)

res_dict2 = {key:list(lis1) for key in seq} #through dict comprehension
print("through dict comprehension",res_dict2)

l = 1
dic1 = {1:'Dilip',2:'Voruganti'}
print("Get the value from key::::::::",dic1.get(3,0))
d = dic1.setdefault(l)

li = [1,2,3,2,8,9,3]
# li1 = [2,3]
li1 = 2
li.append(li1)
print(li)

# # print(li.index(2))
index_list = {}
e_l = []
for i in range(len(li)):
    if(li[i] == 3):
        index_list[i] = li[i]
print(index_list)

for i,value in enumerate(li):
    # if(value==3):
        print("From enumerate",i,value)