import pandas as pd
import csv
import sys
import json
import re

#EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
'''
fieldnames=["hmid"]

csv_filename = "C:/Users/dvoruga/Desktop/Small_CSV.xlsx"
print("Opening CSV file: ",csv_filename)
f = open(csv_filename, 'r')
csv_reader = csv.DictReader(f,fieldnames)
json_filename = csv_filename.split(".")[0]+".json"
print("Saving JSON to file: ",json_filename)
jsonf = open(json_filename,'w')
data = json.dumps([r for r in csv_reader])
jsonf.write(data)
f.close()
jsonf.close()
'''

PYTHONIOENCODING = 'utf-8'

def converToJson(filecsv):
    df = pd.read_csv(filecsv)
    fname = re.sub(r'(.*?\/)(.*)(\_follow.*)(\.csv)',r"\2",filecsv)
    print(fname)
    jsonfile = open("alljson/"+fname+".json",'w')
    jsonfile.write('[')

    L = len(df.index)
    print(L)

    df = df.fillna('')
    df = df.loc[~df['website'.str.contains('recent call') | ~df['website'.str.contains('trace back')]]

#     for i,row in df.iterrows():
#         json.dump(dict(row),jsonfile,ensure_ascii=False)
#         if i<L-1:
#             jsonfile.write(',\n')
#     jsonfile.write(']')
#     jsonfile.close()
# filecsv=sys.argv[1]
# converToJson(filecsv)