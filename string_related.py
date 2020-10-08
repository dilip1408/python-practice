# ## String reverse
# string = "I am Dilip"
# # reversed_str = ''.join(reversed(string))
# # print(reversed_str)
# # # for i in reversed_str:
# # #     print(i)
# # rev = string[::-1]
# # print(rev)
# 
# 
# # index = len(string)
# # print(type(index))
# # rev_str =[]
# # while index > 0:
# #     rev_str += string[index-1]
# #     index = index - 1
# 
# # def reverse(str):
# #     s =""
# #     for i in string:
# #         s = i+s
# #     return s
# #
# # string = "I am Dilip"
# # # reverse(string)
# # print("The reversed string(using loops) is : ",reverse(string))
# 
# # Reverse string using slicing
# # string = 'Dilip'
# # def rev(string):
# #     string = string[::-1]
# #     return string
# #
# # print(rev(string))
# 
# vals = [1,2,3,4,6]
# # print([x*2 for x in vals if x%2])
# 
# #This is equivalent to above list comprehension
# for x in vals:
#     if(x%2==1):
#         print(x*2)
# 
# # a = 5
# # b = 0
# # a,b=b,a
# # print(a,b)
# 
# # a = ("apple", "banana", "cherry")
# # print(type(a))
# 
# # #count-pairs-with-given-sum
# # arr = [0,10,20,30,40,50,60]
# # n = len(arr)
# # sum = 10
# # count = 0
# # for i in range(0,n):
# #     print("This is i ----",i)
# #     for j in range(i+1,n):
# #         if(arr[i] + arr[j]) == sum:
# #             print("This is J---", j)
# #             print(arr[i],arr[j],"And Sum is",sum)
# #             count += 1
# # print("matching count", count)
# # import numpy as arr
# # x = arr.array[(3, 6, 9, 12)]
# # print((x))
# # -----------------
# # #code
# # A = [1, 2, 4, 5, 7]
# # B = [5, 6, 3, 4, 8]
# # lengthA = len(A)
# # lengthB = len(B)
# # sum = 7
# # count = 0
# # def sumpairs():
# #     global count
# #     for i in range(0, lengthA):
# #         for j in range(i+1, lengthA):
# #             if(A[i] + A[j] == sum):
# #                 count += 1
# #
# #     for i in range(0,lengthB):
# #         for j in range(i+1, lengthA):
# #             if(B[i] + B[j] == sum):
# #                 count += 1
# #     return count
# #
# #
# # print(sumpairs())
# 
# # --------------
# # stringA = "Hi Hi welcome"
# # wordtofind = "H"
# # wordtofind1 = "i"
# # count = 0
# # count1 = 0
# # dicttostore ={}
# # print(type(dicttostore))
# 
# # a = stringA.find(wordtofind)
# # print(a)
# # b = stringA.find(wordtofind,0,10)
# # print("This is B value",b)
# # if (stringA.find(wordtofind) != -1):
# #     for i in iter(stringA):
# #         count += 1
# #         print(count)
# #         key = wordtofind
# #         dicttostore[key] = count
# #
# # print(dicttostore)
# 
# # occ = stringA.count(wordtofind)
# # print(occ)
# ##----------------------------
# # class my_dictionary(dict):
# #
# #     # __init__ function
# #     def __init__(self):
# #         self = dict()
# #
# #         # Function to add key:value
# #
# #     def add(self, key, value):
# #         self[key] = value
# #
# #     # Main Function
# #
# #
# # dict_obj = my_dictionary()
# #
# # dict_obj.add(1, 'Geeks')
# # dict_obj.add(2, 'forGeeks')
# #
# # print(dict_obj)
# # ------------------
# 
# # str = "Apple Mango Orange Mango Guava Guava Mango"
# # list1 = str.split()
# # print(list1)
# # list2 = []
# 
# # import json, pandas as pd
# #
# # with open('yarnApplications_12hrs.json') as f:
# #     data = json.load(f)
# # df = pd.DataFrame.from_dict(data, orient='index')
# # df.transpose()
# # # df = pd.read_json('yarnApplications_12hrs.json')
# #
# # print((df))
# 
# # #-----No. of occurance of a character in a string
# print(string)
# dict1 = {}
# dict2 = {1:'Dilip',2:'Voruganti'}
# # str = str.lower()
# 
# a = dict2.keys()
# print(a)
# for i in string:
#     if(i in dict1.keys()):
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print("No. of occurance of a character in a string",dict1)
# 
# # dict3 ={}
# # for keys in str:
# #     dict3[keys] = dict3.get(keys, 0) + 1
# # print(dict3)
# #
# #
# # from collections import Counter
# # count = Counter(str)
# # print(count)
# #
# # test_str = "GeeksforGeeks"
# #
# # # using dict.get() to get count
# # # of each element in string
# # res = {}
# #
# # for keys in test_str:
# #     print(keys)
# #     res[keys] = res.get(keys, 0) + 1
# #
# # # printing result
# # print(res)
# #
# 
# 
# # #Reverse string
# # st = "I am Dilip"
# # rev_st = ''.join(reversed(st))
# # print(st,rev_st)
# # str = st[::-1]
# # print(str)
# # ts=""
# # for i in st:
# #     print(ts,i)
# #     ts = i+ts
# # print(ts)
# 
# # #convert string to Dict
# # string = "key1=value1;key2=value2;key3=value3"
# # # dictionary = dict(x.split("=") for x in str.split(";"))
# # # print(dictionary)
# #
# # for x in string.split(";"):
# #     print(x)
# #     print(x.split("="))
# 
# # str = "key1=value1;key2=value2;key3=value3"
# 
# # d = dict(x.split("=") for x in str.split(";"))
# #
# # for k, v in d.items():
# #     print(k, v)
# 
# import json
# dictionary = '''{
#   "Records": [
#     {
#       "eventVersion": "2.1",
#       "eventSource": "aws:s3",
#       "s3": {
#         "s3SchemaVersion": "1.0",
#         "configurationId": "124ce968-f0e5-465f-9f6d-e2a4db1c4784",
#         "bucket": {
#           "name": "spaceplan-integrationtest",
#           "ownerIdentity": {
#             "principalId": "AWURIUX0P6XPF"
#           },
#           "arn": "arn:aws:s3:::spaceplan-integrationtest"
#         },
#         "object": {
#           "key": "s3-trigger/data.json"
#         }
#       }
#     }
#   ]
# }
# '''
# # data = json.loads(dictionary)
# # file_name = data["Records"][0]["s3"]["object"]["key"]
# # print(file_name)
# 
# # import boto3
# # s3_client = boto3.client('s3')
# # s3_client.put_object()
# 
# sqs = dict({'Records': [{"messageId": '93ca2241-74b5-48a5-aa25-6467073e4c6b', 'receiptHandle': 'AQEBWF5aPrVKvRHYxxPriqRQZ+rsfkTI9TNoLT54myFdYN0RWSoGlRbt2uAZVqKjSyqBj2gyRe+F5aw72lJkjtcLMQxqApwiEug5ov8s3Y6jtGj47W41izOWRU+1uvLHuR9teGAsWMu1HhS7mOf4F/9j2wx9c12EWh+CcXmHDzcQTRqwLif5RGdizavECWZu71ET7N+2LT85wvVRmyVyY4lV6ZYlvGEs6BnxL9xB09eWQMphc3jcyPG/sKeNzr1fdWcR5FcKSIJsIxTVi9Zaug+MPeB3wf02Tw7TlGLg28bVkgO6J7D0DKfTCmxKLafTCs602d2XRRWIZa7DmxFUhY5mNP9sd0EiD+UYQC9AHsZ+UTvRIG6/u/ianzwHGPEmLdH3jhQOT9btbDprEs9YfKe2Ng==', 'body': "{'Name':'Dilip','App':'space'}", 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1592980641453', 'SenderId': 'AROAVEYH7FY4SEW4MMYLD:dvoruga', 'ApproximateFirstReceiveTimestamp': '1592980641457'}, 'messageAttributes': {}, 'md5OfBody': '705bd89d4e47e1ddebe339c922598a6f', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-2:353814654521:spaceplan_integration_test', 'awsRegion': 'us-east-2'}]})
# print(type(sqs))
# # data1 = json.loads(sqs)
# length = int(len(sqs['Records']))
# print(length)
# data1 = sqs['Records'][0]['body']
# print(data1)
