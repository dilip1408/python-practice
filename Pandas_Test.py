# import pandas as pd
# import dateutil
#
# # Load data from csv file
# data = pd.read_csv('C:\\Users\dvoruga\Downloads\phone_data.csv')
# # Convert date from string to date times
# data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)
# print(data)

# #import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data)
# print(s)

#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data,index=[100,200,300,400])
# print (s)

# https://www.geeksforgeeks.org/python-data-analysis-using-pandas/
#As series is 1D array, we can have only index not the columns.
import pandas as pd
# Data =[1,2,3]
# Index = ['a','b','c']
# a = pd.Series(Data,index=Index)
# print(a)
#
# # when data contains dictionary
#
# dictionary= {'a':4,'b':5,'c':6}
# a= pd.Series(dictionary)
# print(a)
#
# #when data contains Ndarray, ## Creating series of 2darray
# Data = [[2,4,6],[1,3,5]]
# print(pd.Series(Data))

# Program to Create Data Frame with two dictionaries
# dict1 ={'a':1, 'b':2, 'c':3, 'd':4}        # Define Dictionary 1
# dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2
# Data = {'first':dict1, 'second':dict2}  # Define Data with dict1 and dict2
# df = pd.DataFrame.from_dict(Data)  # Create DataFrame
# print(df)

# Program to create Dataframe of three series
# import pandas as pd
#
# s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])  # Define series 1
# s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])  # Define series 2
# s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])  # Define series 3
#
# Data = {'first': s1, 'second': s2, 'Third': s3}  # Define Data
# dfseries = pd.DataFrame(Data)  # Create DataFrame
# print(dfseries)
#
# pd.set_option('display.max_rows',19)
# pd.set_option('display.precision',11)
# data = pd.read_csv("C:/Users/dvoruga/Downloads/nba.csv")
# print(data.shape)
# columns = list(data)
# print(columns)
# second = data["Age"]
# #
# print(second)
# print(data.head())
'''
Concatenating DataFrame by setting logic on axes :
In order to concat dataframe, we have to set different logic on axes. We can set axes in the following three ways:

Taking the union of them all, join='outer'. This is the default option as it results in zero information loss.
Taking the intersection, join='inner'.
Use a specific index, as passed to the join_axesset argument
'''
# importing pandas module
import pandas as pd 
pd.set_option('display.max_columns',11)
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

print(df, "\n\n", df1)

# applying concat with axes
# join = 'inner'
res2 = pd.concat([df, df1], axis=1, join='inner')

print(res2)

# using a .concat for
# union of dataframe
res2 = pd.concat([df, df1], axis=1) # By default union will be applied
print(res2)

# res3 = pd.concat([df, df1], axis=1,join_axes=[df.index]) # The index which is matching in df1 will be pulled. join_axes is deprecated
# print(res3)


#Test for replacig with a different string in ONLY ONE COLUMN---
data11 = {'a':['Exist', 'Both', 'Modified'],
        'b':['tts', 'tst', 'tss']}

dat = pd.DataFrame(data11)
dat['a'] = dat.apply(lambda x: x['a'].replace('Exist','Modified'), axis=1)
print(dat)
#Test for replacig with a different string in ONLY ONE COLUMN---End