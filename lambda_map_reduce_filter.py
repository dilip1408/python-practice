g = (lambda x: x*x*x)
print(g(7))

d = filter(lambda x:(x>=3),[1,2,3,4,5,6])
print(list(d))

e = list(filter(lambda x : (x/3==2), [1,2,3,4,5,6,12,9]))
print(e)

e = list(map(lambda x : x/3==2, [1,2,3,4,5,6])) #This returns boolean values, need to check further.
print(e)

e = list(map(lambda x : x*2, [1,2,3,4,5,6]))
print(e)

e = list(filter(lambda x : x*2, [1,2,3,4,5,6]))
print(e)