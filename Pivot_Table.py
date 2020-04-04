import pandas as pd
import numpy as np

df = pd.read_excel("C:/Users/dvoruga/Desktop/uploadS3/sales-funnel.xlsx")

#df = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/7612575181/Dilip/offer_graph_Copy.csv")

#print(df.head())
#print(df['Status'].head())
#df['Status'] = df['Status'].astype('category')
df["Status"] = df["Status"].astype("category")
print(df.dtypes)
df['Status'].cat.set_categories(["won","pending","presented","declined"],inplace=True)

pd.pivot_table(df,index=["Name"])
pi=pd.pivot_table(df,index=["Name","Rep","Manager"])
#print(pi)
