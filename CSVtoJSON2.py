import csv,json
import pandas as pd
import numpy as np

#print(json.dumps(list(csv.reader(open('C:/Users/dvoruga/Desktop/Book1.csv')))))


'''
#for creating the JSON object from CSV
f = open('C:/Users/dvoruga/Desktop/Book1.csv', 'r')
reader = csv.DictReader(f)

jsonoutput = 'C:/Users/dvoruga/Desktop/Book1.json'
with open(jsonoutput, 'a') as f:
    for x in reader:
        json.dump(x, f)
        f.write('\n')

'''

#df = pd.read_csv("C:/Users/dvoruga/Desktop/Book1.csv")
ksn_group_id_data = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/ksn_group_id_data1.csv")
points_data = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/points_data.csv")
#To print multiple columns of a dataframe  '[[]]'(double) is mandatory
#print(df[['Name','test']])


#print(type(points_data))
'''
ksn_group_id = "C:/Users/dvoruga/Desktop/uploadS3/ksn_group_id_data1.csv"
points = "C:/Users/dvoruga/Desktop/uploadS3/Pat5.csv"

list1 = [ksn_group_id, points]
counter = 0
ksn_group_id_data = pd.DataFrame()
points_data = pd.DataFrame()
for file in list1:
    fileToRead = pd.read_csv(file)
    #logic
    if(counter == 0):
        ksn_group_id_data1 = fileToRead
        print("reading first file")
        ksn_group_id_data = ksn_group_id_data.append(ksn_group_id_data1, ignore_index = True)
        print(type(ksn_group_id_data))
        print(counter)
        counter = counter+1
    else:
        points_data1 = fileToRead
        print("y value is:::::::::::::::")
        points_data = points_data.append(points_data1, ignore_index = True)
        print(type(points_data))
        print(counter)
'''

ksn_points_join = pd.merge(ksn_group_id_data, points_data, on='ksn_id', how='left')

ksn_points_join['points_value'] = ksn_points_join['points_value'].apply(lambda x: x if not pd.isnull(x) else 0)

#ksn_points_join = ksn_points_join.points_value.replace(np.NaN, '0')

gen_group_points_data = ksn_points_join.groupby(['group_id','group_by'], as_index=False)['points_value'].sum()

#print(gen_group_points_data)

print(gen_group_points_data.to_json(orient='records'))




#df.Age.replace(np.NaN, 'Is Null value', inplace=True)

# Or, depending on your needs:
#df['Age'] = df.Age.replace(np.NaN, 'Is Null value')

#print(type(pd.DataFrame(ksn_points_join["points_value"].fillna("0"))))

#print(ksn_points_join["points_value"].fillna(0, inplace = True))

#df.replace(to_replace ="Boston Celtics",value ="Omega Warrior")

#gen_ksn_points_join = ksn_points_join.loc[(ksn_points_join['points_value'].isnull())]


#datatypes of columns in Dataframe
#g = ksn_points_join.dtypes
#print(ksn_points_join)
#print(gen_ksn_points_join)



'''
d = {'one': [1, 2, 3, 4], 'two': ['a', 'b', 'c','d'], 'three': [1, 2, 3, 4], 'four': ['a', 'b', 'c', 'd']}

df = pd.DataFrame(d)
#print(df[['one','two']])


print(df)
'''