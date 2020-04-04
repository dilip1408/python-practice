import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv('C:/Users/dvoruga/Downloads/Data_Extract_From_World_Development_Indicators/d690a762-e18a-4c22-837e-eeab2da58e3d_Data.csv')
LOAD_PAT_FILE = pd.read_csv('C:/Users/dvoruga/Desktop/uploadS3/Pat5.csv')
#print(df['2016 [YR2016]'].head())

'''
Index(['Series Name', 'Series Code', 'Country Name', 'Country Code',
       '1990 [YR1990]', '2000 [YR2000]', '2009 [YR2009]', '2010 [YR2010]',
       '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]',
       '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]'],
      dtype='object')

'''
print(df['Country Name'].head())
df.set_index(['Country Code'])
sd = df.reindex(columns=['2010','2011'])

db = sd.diff(axis=1)
db.plot(kind='bar')
plt.show()