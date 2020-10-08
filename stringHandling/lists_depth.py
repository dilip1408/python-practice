# dic = {'Name':'Dilip','age':30}
# print(type(dic))
# d = dic.items()
# print(type(d))
# print((dic))

# These list elements are all of the same type
# Use the slice notation like this
# # These list elements are all of the same type
# zoo = ['bear', 'lion', 'panda', 'zebra']
#
# # But these list elements are not
# biggerZoo = ['bear', 'lion', 'panda', 'zebra', ['chimpanzees', 'gorillas', 'orangutans', 'gibbons']]
#
# someZooAnimals = biggerZoo[2: ]
#
# # Print to see what you exactly select from `biggerZoo`
# print(someZooAnimals)
#
# # Try putting 2 on the other side of the colon
# otherZooAnimals = biggerZoo[:2]
#
# # Print to see what you're getting back
# print(otherZooAnimals)
#
# l = [1,2,3]
# s = ''.join(str(n) for n in l)
# ss = str(l)
# print(ss.split())
# print(type(ss))
# s.split()
# print(type(s))
import pandas as pd

d = {'A':[1,2,3]}
df = pd.CategoricalDtype(['df'])
print(df)