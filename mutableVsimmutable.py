x = 10
y = x

x = x+1
print(id(x))
print(id(y))

list1 = [1,2]

list2 = list1
print(id(list1))
print(id(list2))
list1.append(3)
print(id(list1))
print(id(list2))

print(list1)

tup =(1,2,["a"])
print(id(tup))
print((tup))
# tup[2] = 3

tup[2].append("b")
print((tup))
print(id(tup))

tup3 =(1)
print(type(tup3))