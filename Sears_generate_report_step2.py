import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 22)

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

season_end_wk_string = str(season_end_wk)
season_start_wk_string = str(season_start_wk)

offer_graph = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/7612575181/Dilip/offer_graph_Copy.csv")
offer_tab = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/7612575181/Dilip/offer_tab_Copy.csv")

#To Get all columns after applying the below conditions use the commented 2 lines(All Columns, Filtered column). This is to get filtered columns after applying the filtering conditiond on data(rows)
#offer = offer_tab.loc[(offer_tab['corr'] > corr_fx) & (offer_tab['ini_buy'] > ini_buy_fx) & (offer_tab['ss_per'] > ss_per_fix) & (offer_tab['sellthru'] >= st_fx), ['OFR_ID','l3w_ratio']]
offer = offer_tab.loc[(offer_tab['corr'] > corr_fx) & (offer_tab['ini_buy'] > ini_buy_fx) & (offer_tab['ss_per'] >= ss_per_fix) & (offer_tab['sellthru'] >= st_fx)]
#Filtering the columns
off = offer[['OFR_ID','l3w_ratio']]
#print((off))
#filtering the columns using method.
#off = offer.filter(items=['OFR_ID','l3w_ratio'])

#Refer to the offer comment.
depth = offer_graph.loc[(offer_graph['wk_no'] <= yr_wk) & (offer_graph['wk_no'] >= previous_three_wk), ['OFR_ID','depth','act_units']]
depth['depth_act_units']=depth['depth']*depth['act_units']
print("depth::::::::::",depth)
depth_agg=depth.groupby(['OFR_ID']).sum()

print("depth_agg::::::::::::::",depth_agg)

#print("act_units::::::::",depth_agg['act_units'])
##print("depth_act_units:::::::::",depth_agg['depth_act_units']/depth_agg['act_units'])
depth = (depth_agg['depth_act_units']/depth_agg['act_units'])
depth = pd.DataFrame(depth).reset_index()
depth.rename(columns={0:"depth_units"}, inplace=True) #In R columnn "depth_units" is "depth".

#print(depth) #---
graph = pd.merge(offer_graph,off, on='OFR_ID', how='left')
#print("Graph after marge--------",graph)
#To remove the rows against the column("l3w_ratio) when holding Nan(NULL) values.
graph.dropna(subset=['l3w_ratio'], inplace=True)
#print("graph---------", graph)


#graph[,std_units:=sum(act_units),by=OFR_ID]
graph['std_units'] = graph.groupby('OFR_ID')['act_units'].transform(sum)
#print(graph)

graph = graph.loc[(graph['wk_no'] > yr_wk)]
#print((graph.dtypes))
#df['a'].astype('int64')

graph['exp'] = pd.to_numeric(graph['tg_units']) * pd.to_numeric(graph['l3w_ratio'])
#print(graph)
#graph['exp'] = (graph['tg_units']) * (graph['l3w_ratio'])
#exp<-graph[wk_no== top_wk][,c('OFR_ID','exp','std_units','ini_pro'),with=F]
exp = graph.loc[(graph['wk_no'] == top_wk), ['OFR_ID','exp','std_units','ini_pro']]
print("exp...before join:::::::::::\n",exp)
print("depth... before join::::::::::\n",depth)
exp = pd.merge(exp,depth,on='OFR_ID', how='left')
print("exp...after join::::::::::::::\n",exp)
#exp[,sellthru:=std_units/ini_pro]
exp['sellthru'] = exp['std_units'] / exp['ini_pro']
#exp<-exp[!is.na(exp)]
exp.dropna(subset=['exp'], inplace=True)

k = graph.loc[(graph['wk_no'] == top_wk), ['OFR_ID','exp']]
#print("exp------\n",exp)
#print("KKKK -----------\n", k)
k.dropna(subset=['exp'], inplace=True)

#k['k_exp'] = k['exp']
#Rename is not required as pandas is converting by itself as columnname_x, columnname_y. 
###k1 = k.rename(columns={"exp": "exp_k"})
#k1.dropna(subset=['exp_k'], inplace=True)
#print(graph)
#print("K1------",k1)

#> graph<-merge(graph,k,by='OFR_ID',all=F)
#Inner-join
graph = pd.merge(graph,k,on='OFR_ID',how='inner')

graph['sea'] = graph['exp_x'] / graph['exp_y']
#print(graph)
#print(type(graph['wk_no']))

#print("season_end_wk_string", int(season_end_wk_string[0:4]+"00"))
#print(type(season_end_wk_string))


#print("season_start_wk_string",(int(season_start_wk_string[0:4]+str(total_wk))))

#graph['wk'] = graph.apply(lambda x: (graph['wk_no'] - yr_wk) if graph['wk_no'] <=(int(season_end_wk_string[0:4]+"00")) else ((graph['wk_no']-(int(season_end_wk_string[0:4]+"00"))) + ((int(season_end_wk_string[0:4]+str(total_wk)))) - yr_wk))

#201902

def comp(graph):
    if graph['wk_no'] <=(int(season_end_wk_string[0:4]+"00")):
        val = (graph['wk_no'] - yr_wk)
    else:
        val = ((graph['wk_no']-(int(season_end_wk_string[0:4]+"00"))) + ((int(season_start_wk_string[0:4]+str(total_wk)))) - yr_wk)
    return val
graph['wk'] = graph.apply(comp,axis=1)

#print(graph)
#Both crosstab and pivot table produces same result here.
table = pd.crosstab([graph['OFR_ID']],columns=graph['wk'], values=graph['sea'], aggfunc=[np.mean])
#table = pd.pivot_table(graph, index=["OFR_ID"], columns=["wk"], values=["sea"], aggfunc=[np.mean])
print((table.describe))

#mx<-matrix(0,nrow=nrow(sea),ncol=39-(ncol(sea)-1))
row_count = table.shape[0]  # gives number of row count
print("Row Count::::", row_count)

Column_count = table.shape[1]
print("Column Count::::", Column_count)
mx = pd.DataFrame(columns=[row_count])
print("MX Dataframe",mx)

col = 39-Column_count

data = pd.DataFrame(pd.np.empty((row_count, col)) * 0)
print("Data:",data)

#my_df  = pd.DataFrame(columns = col_names)

'''
############# Class level ################################

class_graph = pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/7612575181/Dilip/class_graph.csv")
class_tab= pd.read_csv("C:/Users/dvoruga/Desktop/uploadS3/7612575181/Dilip/class_tab.csv")
class_tab = class_tab[(class_tab['corr'] > corr_fx) & (class_tab['ini_buy'] > ini_buy_fx) &( class_tab['ss_per'] >= ss_per_fix) &( class_tab['sellthru'] >= st_fx)]
off = class_tab[['sub_id','l3w_ratio']]

depth = class_graph.loc[(class_graph['wk_no']<= yr_wk) & (class_graph['wk_no'] >= previous_three_wk),['sub_id','depth','act_units']]

depth['depth_act_units'] = depth['depth'] * depth['act_units']
depth_agg = depth.groupby('sub_id').sum()

#print(depth['depth_act_units'] / depth['act_units'])
depth = (depth_agg['depth_act_units']/depth_agg['act_units']).reset_index()
depth.rename(columns={0:"depth_units"}, inplace=True)
#print(depth.head())

#graph<-merge(graph,off,by='sub_id',all.x=T,allow.cartesian=TRUE)
#graph = pd.merge(offer_graph,off, on='OFR_ID', how='left')
class_graph = pd.merge(class_graph, off, on='sub_id', how='left')

#graph<-graph[!is.na(l3w_ratio)]

class_graph.dropna(subset=['l3w_ratio'], inplace=True)
class_graph['std_units'] = class_graph.groupby(['sub_id'])['act_units'].transform(sum)


class_graph = class_graph[(class_graph['wk_no'] > yr_wk)]
class_graph['exp'] = pd.to_numeric(class_graph['tg_units']) * pd.to_numeric(class_graph['l3w_ratio'])


#class_graph.to_csv('C:/Users/dvoruga/Desktop/uploadS3/7612575181/test_graph_step2.csv', sep=',', encoding='utf-8')

exp_1 = class_graph.loc[(class_graph['wk_no'] == top_wk),['sub_id','exp','std_units','ini_pro']]

exp_1 = pd.merge(exp_1,depth,on='sub_id', how='left')
exp_1['sellthru'] = exp_1['std_units'] / exp_1['ini_pro']



k = class_graph.loc[(class_graph['wk_no'] == top_wk),['sub_id','exp']]

class_graph = pd.merge(class_graph,k, on='sub_id',how='inner')

class_graph['sea'] = class_graph['exp_x'] / class_graph['exp_y']


def comp(class_graph):
    if[class_graph['wk_no'] < (int(season_end_wk_string[0:4]+"00"))]:
        val = (class_graph['wk_no'] - yr_wk)
    else:
        val = (class_graph['wk_no'] - (int(season_end_wk_string[0:4]+"00"))) + ((int(season_start_wk_string[0:4]+total_wk))-yr_wk)
    return val

class_graph['wk'] = class_graph.apply(comp,axis=1)
print(class_graph)

#class_graph1 = pd.crosstab(index=class_graph['sub_id'],columns=[class_graph['wk']])
table = pd.crosstab([class_graph['sub_id']],columns=class_graph['wk'], values=class_graph['sea'], aggfunc=[np.mean])

#table = pd.pivot_table(class_graph,index=['sub_id','wk'],values=["sea"],aggfunc=[np.mean])

print(table)

#sea<-cast(graph,sub_id~wk,mean,value='sea')
'''