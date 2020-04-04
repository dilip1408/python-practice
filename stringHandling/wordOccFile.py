text = open("C:\\Users\dvoruga\Downloads\FileHandling.txt","r")

# One way of doing it-------
# d = dict()
# for line in text:
#     line = line.strip()
#     line = line.lower()
#     words = line.split(" ")
#     print(words)
#     for word in words:
#         if word in d:
#             d[word] += 1
#         else:
#             d[word] = 1
# print(d)




#-------------------------------------------------
#other way-------------

#----------------
# dic = {'Name':'Dilip','age':30}
# print(type(dic))
# d = dic.items()
# print(type(d))
# print((dic))

# # These list elements are all of the same type
# # Use the slice notation like this
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

import json
event = {'Records': [{'messageId': '76e022ba-9d10-4e57-a0f7-8236e4162b43', 'receiptHandle': 'AQEBDh4aCLW9DMZg0oBxddeSGVyMt0JRDfG0b3UahE6NqQMjb2GKnzXeNG4HaAAl4nTv+GDdZIHuzctzVXWGpJGsUx7gsffIntBi4jMGeoXI9T1GzXTACkFBocJwxBgz39nu8OlUHVofljZ0tj+muzmrg+DX7wsgm65lFa/WY9/RAlo/+zhqiU02QAdL3rslq+2gpo9EDdIiVVda/cN8YEq9BCyH6jFx2aslpLa27I5a5DqpMkHWLQZ/kNf8l+1uNoYokHgC/U2bjN+R0u9na2eHb8NaEImwa/JWdZ1eJDNfwLWtfGtmqtW6I5u/8j8p/QCNIEuL66AlneqG8XEeHqEQyXO6mWAjZVoAoFWHWtBvpkd7xONItnzsDjmWSkRhqbtTK/ffGfC7V0rLKph7guh80w==', 'body': '{\n  "div_no": "999999999",\n  "item_no": "444444444444444"\n}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1574948943406', 'SenderId': 'AROAVEYH7FY4SEW4MMYLD:dvoruga', 'ApproximateFirstReceiveTimestamp': '1574948943410'}, 'messageAttributes': {}, 'md5OfBody': 'bb4d2ae8bc0d40c6c08a73f1708c9ce9', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-2:353814654521:spaceplan-test', 'awsRegion': 'us-east-2'}]}
# print("Event::::",type(event),event)
# print(type(event['Records']), event['Records'])
# print(type(event['Records'][0]), event['Records'][0])
# print("eventSource::::",type(event['Records'][0]['eventSource']), event['Records'][0]['eventSource'])
# print("body::::",type(event['Records'][0]['body']), event['Records'][0]['body'])

container={}
x = 5
def lambda_handler(event,context):
    print(context)
    if (event['Records'][0]['eventSource'] == 'aws:sqs'):
        body = event['Records'][0]['body']
        input = json.loads(str(body))
        # print(type(input))
        # print(x)
        div_no = input["div_no"]
        item_no = input["item_no"]
        # print(div_no,item_no)
    else:
        div_no = event["div_no"]
        item_no = event["item_no"]
    container['div_no_is'] = [div_no]
    container['item_no_is'] = [item_no]
    print(container)
    return container


lambda_handler(event,context="Hi")
# event1 = {'Records':[{'msg':'Hi','mainsrc':{"src":'SQS','exe':'D'}}]}
#
# print(type(event1['Records'][0]['mainsrc']),event1['Records'][0]['mainsrc'])
#
# d = {"div_no": "999999999","item_no": "444444444444444"}
# print(type(d))
#
# body = '{ "div_no": "999999999",  "item_no": "444444444444444"}'
# print(type(body),body)

# event = {'Records': [{'messageId': '316712f4-cbd6-4781-b13a-f6881c86b8f2', 'receiptHandle': 'AQEBlsBiSG67Kn6pylQIoQAqfhWVm+MjWAJaMQLFUf8g+0jza+TF2vzTsD2jJMFaU5aBEzAWPUb468YnHW3MoPD3frRUJiuntEYdU+74j0OFc87Jf9R+O1gux8/LTrPRmX3dn1mFyNIoXPdjud7ktpZxGzg9d4hjwkVNDJYaHv/+V+l2Jt+vSu+Vpmw5co09VjyO2jZtydyQejyUceQOfZt/MvQy8xfIHW+PqdUZf75/TrTf7llqkILsLdx+aguWh0SrwkUcU+AN3QJ9ekXSzRen3ld36Khk/6nQDY3KVdZfOUt/7tJvWeO4TPRBy8aSEO9Pv9q6Mlk54amrlyJFUu7pLtAAsCVngEkmqfff+gIBbqxMHuNG2Q5Lvf/bvJirLnaL19P3J9psmp5uwy/m2Fw20/w1ENYKoM4cRSFlL8ix7xE=', 'body': '{"div_no": 17, "itm_no": 23405, "loc_no": 1088, "eff_date": "2019-09-26,2019-10-24,2019-11-28,2019-12-26,9999-12-31,9999-12-31,9999-12-31,9999-12-31,9999-12-31,2019-12-31", "markdown_weeks": "201934,201938,201943,201947,999999,999999,999999,999999,999999,201948", "plan_name": "519 607 09-26-2019 ts MAN TEST NAVEEN", "season_cd": 5, "num_week_sales": 52, "onlywinner": "Y", "end_date": "2019-12-31", "ssn_name": "FW", "week_ssn_start": 201818, "effective_date": "2019-10-03", "mdl_name": "SearsAplFW", "bu": "Apl"}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1569323163526', 'SenderId': 'AROAISFWKLC7UUMFEM7KW:entpric_testSampleCode', 'ApproximateFirstReceiveTimestamp': '1569323209200'}, 'messageAttributes': {}, 'md5OfBody': '04ceaa857308863971e2e767cb683f6a', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-2:353814654521:entpric-clxprc-sears-PlanData', 'awsRegion': 'us-east-2'}]}
# print(type(event['Records'][0]['body']),event['Records'][0]['body'])


