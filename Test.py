'''
import pandas as pd
import numpy as np



#52 201852 201903 201814 52 201851 201850 201901 201902 201918 201903
current_wk = 2
yr_wk = 201902
model_wk = 201905
season_start_wk = 201814
total_wk = 52
previous_two_wk = 201901
previous_three_wk = 201852
top_wk = 201903
top_next_week = 201904
season_end_wk = 201923
clx_wk = 201911

endwk_fix=total_wk
#SC=c(4,5)
ini_buy_fx=1000############change
corr_fx=0.8################change

##assumption##
sc=0.92
st_fx=0.08
ss_per_fix=0.7

offer_graph = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/7612575181/Dilip/offer_graph.csv")
offer_tab = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/7612575181/Dilip/offer_tab.csv")

#To Get all columns after applying the below conditions use the commented 2 lines(All Columns, Filtered column). This is to get filtered columns after applying the filtering conditiond on data(rows)
offer = offer_tab.loc[(offer_tab['corr'] > corr_fx) & (offer_tab['ini_buy'] > ini_buy_fx) & (offer_tab['ss_per'] > ss_per_fix) & (offer_tab['sellthru'] >= st_fx), ['OFR_ID','l3w_ratio']]
#Refer to the offer comment.
depth = offer_graph.loc[(offer_graph['wk_no'] <= yr_wk) & (offer_graph['wk_no'] >= previous_three_wk), ['OFR_ID','depth','act_units']]

#print(type(depth))

#depth<-depth[,list(depth=sum(depth*act_units)/sum(act_units)),by=OFR_ID]

#multiply = sum(depth['depth'] * depth['act_units']) / sum(depth['act_units'])


#depth1 = depth.groupby('OFR_ID'). depth.mul(depth'* "act_units"}).agg({"act_units" : "sum"})
depth1 = depth.groupby('OFR_ID')
#df = pd.DataFrame(depth1)
#df['count'] = sum(df['depth'] * df['act_units']) / sum(df['act_units'])
print(type(depth1))
print("depth1:::::", depth1)


current_wk = 2
yr_wk = 201902
model_wk = 201905
season_start_wk = 201814
total_wk = 52
previous_two_wk = 201901
previous_three_wk = 201852
top_wk = 201903
top_next_week = 201904
season_end_wk = 201923
clx_wk = 201911



#x= season_end_wk[:4]
number_string = str(season_end_wk)
print(int(number_string[0:4]+"00"))
print(type(number_string))

graph['wk'] = graph.apply(lambda x: 'True' if x <= 4 else 'False')

#201902

#graph[,wk:= ifelse( wk_no< as.integer(paste(substr(season_end_wk,0,4),"00",sep="")),(wk_no - yr_wk),(wk_no-as.integer(paste(substr(season_end_wk,0,4),"00",sep=""))+as.integer(paste(substr(season_start_wk,0,4),total_wk,sep=""))-yr_wk))]  #This
'''

'''
import pandas as pd
#pd.set_option('display.max_columns', 6)
studentAgeData = {'TIMESTAMP': {0: '2019-02-15 03:07:03.662 +0000', 1: '2019-02-15 03:07:06.824 +0000'}, 'MD5(SESSION_ID)': {0: '60584c4ed725b4554397e3a99ecf79bb', 1: '599c2b8af6715568f69d9a1b9e0adfc1'}, 'EVENT_NAME': {0: 'my_news_card_viewed', 1: 'top_news_card_viewed'}, 'MD5(USER_ID)': {0: '3dd1b5078d31866877edbc1259523dcf', 1: '5ff49205bb31da8ef1c8ac1cbf3aee14'}, 'ATTRIBUTES': {0: '{    "category": "digital_life",    "id": "jLcW_MnCfbLN8Ph-bsTwGw",    "noteType": "TRENDING_SOCIAL",    "orientation": "PORTRAIT",    "position": "1",    "publishTime": "2019-02-14T21:08:00Z",    "sourceDomain": "gamestar.de",    "sourceName": "GameStar",    "stream": "wtk",    "streamType": "my news", "title": "News: Overwatch League - 2. Saison startet heute Nacht, ein einziger deutscher Spieler ist dabei",    "url": "https://www.gamestar.de/artikel/overwatch-league-2-saison-startet-heute-nacht-ein-einziger-deutscher-spieler-ist-dabei,3340648.amp"  }', 1: '{    "category": "politics",    "id": "46382c96-8913-4fe6-bcc7-8bc2a4e98b34",    "orientation": "PORTRAIT",    "position": "1",    "publishTime": "2019-02-15T00:01:55Z",    "sourceDomain": "mirror.co.uk",    "sourceName": "Mirror",    "stream": "ntk",    "subcategories": [],    "title": "May\'s Brexit plan: What happens now?",    "url": "https://www.mirror.co.uk/news/politics/brexit-what-happened-theresa-mays-14000631"  }'}}

df  = pd.DataFrame.from_dict(studentAgeData)
#df = pd.DataFrame.from_records([[i, j] + d[i][j] for i in d for j in d[i]])
#dfObj = pd.DataFrame(list(studentAgeData.items()), index=['a', 'b', 'c', 'd', 'e'])
# Create dataframe from dic and make keys, index in dataframe
#dfObj = pd.DataFrame.from_dict(studentAgeData, orient='index')
#print(df_data)

#df = pd.DataFrame.from_dict({(i,j): user_dict[i][j]
 #                       for i in user_dict.keys()
  #                      for j in user_dict[i].keys()},
   #                    orient='index')

print(df)
df1 = df['ATTRIBUTES']

#df1 = df1['ATTRIBUTES'].str[3:]
print(df1)

dictionary = df1.to_dict()
print(dictionary)
'''

''' -- To count no of capital letters--
import os
os.chdir("C:/Users/dvoruga/Desktop")
with open('python.txt') as file:
    count = 0
    for i in file.read():
        if i.isupper():
            print(i)
            count = count+1

    print(count)
'''
'''
String = '1,2,3,4,5'
s= ','.split(String)
print(s)

string = 'Geeks for Geeks'
spli = string.split(' ')
print(spli)
st = '-'.join(spli)
print(st)
'''

# DO NOT TINKER
import os
'''
# numpy for array manimulation and pandas for file loading and data manipulation
import numpy as np
import pandas as pd
import time
import math

# Keras models for neural network creation and learning
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.wrappers.scikit_learn import KerasRegressor
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
import keras.backend as K
from keras.layers import Dense, Activation, Flatten, Convolution1D, Dropout
from sklearn.cluster import KMeans
from keras.callbacks import EarlyStopping
from keras import regularizers
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MinMaxScaler

# matplotlib for plotting the graphs
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import warnings
from keras.models import load_model
warnings.filterwarnings('ignore')

import locale
locale.setlocale( locale.LC_ALL, '' )
pd.set_option('display.float_format', lambda x: '%.3f' % x)
'''


# string = "I am :- Dilip Voruganti"
#
# print(list(string))
# print(string.split("-"))
#
# import random
# list = [2, 18, 8, 4]
# print ("Prior Shuffling - 0", list)
# random.shuffle(list)
# print ("After Shuffling - 1", list)
# random.shuffle(list)
# print ("After Shuffling - 2", list)

#List Comprehensions- Comprehensions can be implemented through Lists,Dict and sets
# num = [1,2,3,4,5,6,7,8,9,10]
# my_list=[]
# # for n in num:
# #     my_list.append(n*n)
# my_list = [n*n for n in num]
# print(my_list)
########
# for n in num:
#     if(n%2==0):
#         my_list.append(n)
# my_list=[item for item in num if item%2 ==0]
# print(my_list)
################

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# my_list =[(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

#Dictionary Comprehensions
# Names = ['Aamir Khan','Akshay Kumar','Ajay Devgn','Amjad Khan','Amitabh Bachchan']
# Heros = ['Lagaan','Baby','Shivaay','Sholay','Black']
# my_dict={}
# for Name,Hero in zip(Names,Heros):
#     my_dict[Name] = Hero
# print(my_dict)
# my_dict={Name:Hero for Name,Hero in zip(Names,Heros) if(Name!='Amjad Khan')}
# print(my_dict)

# item=[]
# item=[n*2 for n in range(10)]
# my_dict={}
# my_dict={n: n*2 for n in range(10)}
# print(item)
# print(my_dict)

#set  Comprehension
# my_set = set()


###
# import pandas as pd
# tup = (("Dilip",32),("Dil",31),("Voruganti",30))
# print(type(tup))
# tup_dict =dict(tup)
# print(tup_dict)
# tup_df = pd.DataFrame(tup)
# print(tup_df)

# names = ['Dilip', 'Ravali']
# surname = ['voruganti','Samudrala']
# my_dict = {name:surname for name,surname in zip(names,surname) if(name != 'Ravali')}
# print(type(my_dict))


# print(sorted(ll))
# sett = {1,2,'a','b'}
# print(type(sett))
#
# li = [1,2]
# # li1 = [2,3]
# li1 = 2
# li.append(li1)
# print(li)

# ll = [5,2,6,8,1,2,9]
# y = map(lambda x: x*x, [5])
# print(list(y))
#
# p = lambda x,y,z: x*2 + y*2 + z*2
# print(p(2,2,2))
#
# numbers = [1, 2, 3]
# print(list(map(lambda x: x*3==9,numbers)))
#
# print(list(map(lambda x : (x*2==4), [1,2,3,4,5,6])))

# for i in range(4):
#     for j in range(4-i):
#         print("#", end=" ")
#     print()

# for i in range(10):
#     if i%2 == 0:
#         pass
#     else:
#         print(i)

###########Diff  b/w pass and continue ###########
# x = [1,2,3,4]
# for i in x:
#     if i==2:
#        pass  #Pass actually does nothing. It continues to execute statements below it.
#     print("This statement is from pass:::",i)
# for i in x:
#     if i==2:
#         continue #Continue gets back to top of the loop.And statements below continue are executed.
#     print("This statement is from continue:::",i)
#
# # print(0%2)
###################################################
################  Linear search -- details in notes -- Telusko#######
# l = ['a','x','z','a']
#
# length = len(l)
# value = 'z'
# pos = -1
#
# def search_while(l,value):
#     i = 0
#     while i < length:
#         if l[i] == value:
#             globals()['pos'] = i
#             return True
#         i = i + 1
#     return False
#
# def search_for(l,value):
#     for i in range(length):
#         if l[i] == value:
#             globals()['pos'] = i
#             return True
#
#     return False
#
#
#
# if search_for(l,value):
#     print(value,"Found at position",pos)
# else:
#     print(value,"Not Found")
##################################################
# ########### Binary Search -- details in notes -- Telusko ######################
#
# list1 = [3,5,2,8,7,4]
#
# def sort(b_list):
#     for i in range(len(b_list)):
#         for j in range(i+1):
#             if b_list[i] < b_list[j]:
#                 b_list[i],b_list[j] = b_list[j],b_list[i]
#             else:
#                 pass
#     return  b_list
#
#
# sort(list1)
#
# pos = -1
# def search(list1,n):
#     lb = 0
#     ub = len(list1) - 1
#     while lb <= ub:
#         mid = (lb + ub)//2
#         if list1[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list1[mid] < n:
#                 lb = mid + 1
#             else:
#                 ub = mid - 1
#     return False
#
# n = 2
#
# print(list1)
# if search(list1,n):
#     print(n,"Found at position",pos+1)
# else:
#     print(n,"Not Found")
#
# #######################END Binary Search ############
# ##################Bubble sort #################
#
# nums = [2,6,8,3,1,5]
#
# def bubble_sort(nums):
#     #If we use length with range from 0 to x then it starts with 0. but if we use range in reverse order(using -1 in d 3rd step of range), in this case '6' then it starts with 6 and ends till 0. it will be wrong count. so we need to negate with '-1'
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1],nums[j]
#
# print(nums)
# bubble_sort(nums)
# print(nums)
# ##################################
# ############  Binary search -- Practice -- for loop ###########
# # l = [3,2,5,4,1,8]
# l = [1,2,3,4,5,6]
# pos = -1
# value = 5
# def search(l,value):
#     ub = len(l) - 1
#     lb = 0
#
#     for i in range(len(l)):
#         print(l)
#         mid = lb + ub // 2
#         if l[mid] == value:
#             globals()['pos'] = mid
#             print("value found", pos)
#             return True
#         else:
#             if l[mid] > value:
#                 ub = mid
#             else:
#                 lb = mid
#     return False
#
# if search(l,value):
#     print("value found")
# else:
#     print("value not found")
# ################################################

# ########### Ways to reverse a string ##########
# # 1.
# string = 'Dilip Voruganti'
# rv = ''.join(reversed(string))
# print(rv)
# print(string)
#
#
# #2.
# ll = ''
# for i in string:
#     ll = i + ll
# print(ll)
#
# # 3. Recursion
# # print("Recursion:::;reverse(string[1:]) + string[0]", (string[1:]) + s[0])
# # Python code to reverse a string
# # using recursion
#
# # def reverse(s):
# # 	if len(s) == 0:
# # 		return s
# # 	else:
# # 		return reverse(s[1:]) + s[0]
# #
# # s = "Geeksforgeeks"
# #
# # print ("The original string is : ",end="")
# # print (s)
# #
# # print ("The reversed string(using recursion) is : ",end="")
# # print (reverse(s))
#
#
# # 4. Extended slicing
#
# # print("Extended slicing:::::::",string[::-1])
#
# # 5. Another way is using stack,  not implemented here.
##############
# ##### To find min and max numbers-------
#
# l = [5,4,3,6,8,1,2,-2]
# minimum = 0
# maximum = 0
#
# for i in l:
# 	if i > maximum:
# 		maximum = i
# 	else:
# 		minimum = i
# print(minimum,maximum)

###########
######### max even and max odd ######
# l = [5,4,3,6,8,1,2,-2]
# max_even = 0
# max_odd = 0
#
# for i in l:
# 	if i%2==0 and i > max_even:
# 			max_even = i
# 	elif i%2 ==1 and i > max_odd:
# 		max_odd = i
#
# print(max_even,max_odd)
# ######### ######
#
# list1 = [3,2,5,4,6,7]
# list2 = [8,1]
# list1 = list1+list2
#
# length =len(list1)
# for i in range(length):
# 	for j in range(i+1,length):
# 		if list1[i] > list1[j]:
# 			list1[i],list1[j] = list1[j],list1[i]
# 		else:
# 			pass
# print(list1)

# # Import `randrange` from the `random` library
# from random import randrange
#
# # Construct your `randomLetters` variable with a list of the first 4 letters of the alphabet
# randomLetters = ['a','b', 'c', 'd']
#
# # Select a random index from 'randomLetters`
# randomIndex = randrange(0,len(randomLetters))
# print(randomIndex)
#
# # Print your random element from `random`
# print(randomLetters[randomIndex])
#
#
# li1 = ['Dilip','Voruganti']
# li2 = ['Ravali','Samudrala']
#
# d = dict(zip(li1,li2))
# print(d)
#
# import itertools
# friends = ['Team 1', 'Team 2', 'Team 3', 'Team 4']
# print(list(itertools.combinations(friends,3)))
#
#
#
# e = list(filter(lambda x : (x/3==2), [1,2,3,4,5,6,12,9]))
# print(e)
#
# import numpy as np
# ar = np.array([1, 3, 2, 4, 5, 6])
# print(ar.argsort()[-3:][::-1])
#
# x_y_z = 1,000,000
# print(x_y_z)
#

###Cognizant
l = [2,7,1,8,11,7,7,6,7,10,7]
length = len(l)
print(length)
l = [i for i in l if i !=7]
# print(l)
# while 7 in l:
#     l.remove(7)
# print(l)
# l = [2,7,1,8,11,7,7,6,7,10,7]
# x = 0
# for i in l:
#
#     if(i == 7):
#         l.remove(i)
#     leng = len(l)
#     x += 1
#     y = l[x]
#     ll = l.copy()
# print(l)
# for i in range(len(l)):
#     while length > 0:
#         print(l[i])
#         if(l[i]==7):
#             l.remove(l[i])
#         length -= 1
#     print(length)
# print(l)

# for i in l:
#     if(i!=7):
#         print(i)


#What is wrong with this code. There is nothing wrong with this code.
# def reassign(val):
# 	val = [1,2,3,4]
#
# mainval = [4,5,6]
# print(reassign(mainval))

# a=10
# def display():
#     b=20
#     print("global variable", a)
#     print("local variable", b)
#
# display()
# c=30
# print("global variable", a)
# # print("local variable", b)
# print(c)

Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}
Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak','age': 50, 'pay': 50000}

for k in Omkar.items():
    print(type(k))

print(type(Omkar.items()))