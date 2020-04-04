import pandas as pd

#variables Initialization
cumulative_seasonality_value = 0.001
clu = 0
match = 0
end_wk = 201834
sttg = 0.1

LOAD_PAT_FILE = pd.read_csv('C:/Users/dvoruga/Desktop/uploadS3/Pat5.csv')

#pd.set_option('precision', 9)

LOAD_PAT_FILE1 = LOAD_PAT_FILE.rename(columns={'id':'sub_id','wk_indi':'week','st_r':'seasonality'})

#Group by sub_id and apply cumsum on seasonality
LOAD_PAT_FILE1['cum_seasonality'] = LOAD_PAT_FILE1.groupby(['sub_id'],sort='week')['seasonality'].cumsum()

# There is a file generation till this Data set in pig script. I have skipped it.

FILTER_PAT_FILE = LOAD_PAT_FILE1.loc[(LOAD_PAT_FILE1['cum_seasonality'] > cumulative_seasonality_value)]

OUTPUT_MAP_DATA = FILTER_PAT_FILE.filter(items=['sub_id', 'week'])
GRP_DATA = OUTPUT_MAP_DATA.groupby(['sub_id'])

#To get only min(week) records, one record per sub_id
GRP_DATA_MIN = GRP_DATA.apply(lambda x: x.week.min())
GRP_DATA_MIN_DF = pd.DataFrame(GRP_DATA_MIN).reset_index()

GRP_DATA_MIN_DF.loc[:,'clu'] = clu
GRP_DATA_MIN_DF.loc[:,'match'] = match
GRP_DATA_MIN_DF.loc[:,'end_wk'] = end_wk
GRP_DATA_MIN_DF.loc[:,'sttg'] = sttg

GRP_DATA_MIN_DF.rename(columns={0: "min_week" },inplace=True)

print(GRP_DATA_MIN_DF)
print(GRP_DATA_MIN_DF.to_json(orient='records'))