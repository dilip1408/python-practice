import pandas as pd
from pandas.api.types import CategoricalDtype

df_raw = pd.read_csv('C:/Users/dvoruga/Downloads/PGYR17_P011819/OP_DTL_RSRCH_PGYR2017_P01182019.csv', low_memory=False)

#print(list(df_raw.columns))

drop_thresh = df_raw.shape[0]*.9
#df = df_raw.dropna(thresh=drop_thresh, how='all', axis='columns').copy()
print(drop_thresh)