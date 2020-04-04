import json
import boto3
import pandas as pd
from pandas.io.json import json_normalize
import os
import numpy as np

import sys
import auroraDB_config
import pymysql
import sqlalchemy
from pandas.io import sql
from sqlalchemy import create_engine
import xlsxwriter

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

#auroraDB settings
host_name  = auroraDB_config.host_name
name = auroraDB_config.db_username
password = auroraDB_config.db_password
db_name = auroraDB_config.db_name


def lambda_handler(event, context):   
    found=False
    jsonObj=''
    decodedDataNew=''
	
	# Step1 : Extract the entries in the desired S3 bucket and parse the contents to JSON Obj
    for bucket in s3.buckets.all():
        if not found:
            #print("bucket Name:::::",bucket.name)
            if(bucket.name=='entpric-clx-sears'):
                found=True
                mybucket = s3.Bucket(name=bucket.name)                
                for obj in mybucket.objects.all():
                    #print("object::::::::",obj)
                    #print("obj.key::::: ",obj.key)
                    
                    if(obj.key.startswith("2018/12/31/09/entpric_clx_sears_del_stream-5-2018-12-31-09-47-11-b4688d04-bc6f-4338-a105-b6edd005c15e")):
                        data = s3_client.get_object(Bucket=bucket.name, Key=obj.key)
                        decodedData = data['Body'].read().decode("utf-8")
                        decodedDataNew = decodedDataNew+decodedData
                        #print("decodedDataNew:::::::::",decodedDataNew)
    
    decodedDataAll = "[" + decodedDataNew[:-1] + "]"
    jsonObj=json.loads(decodedDataAll)
    #print("jsonObj::::::::::",jsonObj)
    #print("jsonObj decoded Successfully!!")
    
    # Step 2 - Flatten the JSON object such that it could be easily converted to a pandas Dataframe
    flatten_keys = ['prcCombinationLevelOutput']
    a = sometimes_flatten(jsonObj,flatten_keys)
    #print("sometimes_flatten invoked Successfully!!")
    
    # Step 3 - Convert Flatten JSON obj to Dataframe
    df = pd.DataFrame.from_dict(json_normalize(a), orient='columns')
    #print("Flattened JSON obj to Dataframe Successfully!!")
	
	# Step 4 - Store the dataframe to Aurora DB
    #storeDFToDB(df)
    #print("storeDFToDB invoked Successfully!!")
    
    #Split dataframes to initial and subsequent
    df_initial=df.loc[df['optimization.clearanceFlag'] == 0]
    df_sub=df.loc[df['optimization.clearanceFlag'] == 1]
    
	
    # Step 5 - Derive additional fields required for reporting from the original dataframe    
    df['Current_Disc_Bucket'] = df.apply(deriveCurrentDiscountBucket, axis = 1)
    #print("df[Current_Disc_Bucket]::::::",df['Current_Disc_Bucket'])
    #print("df[Current_Disc_Bucket] derived Successfully!!")
    
    df['WoS_Bucket'] = df.apply(deriveWOSBucket, axis = 1)
    #print("df['WoS_Bucket']:::::",df['WoS_Bucket'])
    #print("df[WoS_Bucket] derived Successfully!!")
    #print("df before derivation of MD1::::::::::::",list(df))
    df_1=deriveMD1CombinationsAndAggregate(df,1,'vbs_no','Current_Disc_Bucket',0)
    #df_2=deriveMD1CombinationsAndAggregate(df,df['optimization.prcCombinationLevelOutput_0_md1_units'],'vbs_no','Current_Disc_Bucket',df_1.shape[0]+1)
    #df_3=deriveMD1CombinationsAndAggregate(df,df['optimization.prcCombinationLevelOutput_0_md1_oh'],'vbs_no','Current_Disc_Bucket',df_2.shape[0]+1)
    df_2=deriveMD1CombinationsAndAggregate(df,df['optimization.prcCombinationLevelOutput_0_md1_units'],'vbs_no','Current_Disc_Bucket',18)
    df_3=deriveMD1CombinationsAndAggregate(df,df['optimization.prcCombinationLevelOutput_0_md1_oh'],'vbs_no','Current_Disc_Bucket',36)
    
    
    df['Wt_MD1_Disc_n']=df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice']*(1 - df['optimization.prcCombinationLevelOutput_0_md1'].astype(str).astype(int))
    df['Wt_MD1_Disc_d']=df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice']
    df['Wt_Curr_Disc_n']=df['On_Hand_ToP_wk']*df['optimization.regularPrice']*(1-df['optimization.currentDiscount'])
    df['Wt_Curr_Disc_d']=df['On_Hand_ToP_wk']*df['optimization.regularPrice']
    df['Disc_Change_1n']=df['On_Hand_ToP_wk']*df['optimization.regularPrice']*(1-df['optimization.currentDiscount'])
    df['Disc_Change_1d']=df['On_Hand_ToP_wk']*df['optimization.regularPrice']
    df['Disc_Change_2n']=df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice']*(1-df['optimization.prcCombinationLevelOutput_0_md1'])
    df['Disc_Change_2d']=df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice']
    #print("df before df_diag_report_pivot4::::::",list(df))
    df_diag_report_pivot4 = df[['vbs_no','WoS_Bucket','on_hand_act','Wt_MD1_Disc_n','Wt_MD1_Disc_d','Wt_Curr_Disc_n','Wt_Curr_Disc_d','Disc_Change_1n','Disc_Change_1d','Disc_Change_2n','Disc_Change_2d','optimization.prcCombinationLevelOutput_0_md1_rev','optimization.prcCombinationLevelOutput_0_md2_rev','optimization.prcCombinationLevelOutput_0_md3_rev','optimization.prcCombinationLevelOutput_0_md4_rev','optimization.prcCombinationLevelOutput_0_md5_rev','optimization.prcCombinationLevelOutput_0_md6_rev','optimization.prcCombinationLevelOutput_0_md7_rev','optimization.prcCombinationLevelOutput_0_md8_rev','optimization.prcCombinationLevelOutput_0_md9_rev','sal_value','optimization.prcCombinationLevelOutput_0_md1_cmd','optimization.prcCombinationLevelOutput_0_md2_cmd','optimization.prcCombinationLevelOutput_0_md3_cmd','optimization.prcCombinationLevelOutput_0_md4_cmd','optimization.prcCombinationLevelOutput_0_md5_cmd','optimization.prcCombinationLevelOutput_0_md6_cmd','optimization.prcCombinationLevelOutput_0_md7_cmd','optimization.prcCombinationLevelOutput_0_md8_cmd','optimization.prcCombinationLevelOutput_0_md9_cmd']]
    #df_diag_report_pivot4 = df[['vbs_no','WoS_Bucket','on_hand_act','Wt_MD1_Disc_n','Wt_MD1_Disc_d','Wt_Curr_Disc_n','Wt_Curr_Disc_d','Disc_Change_1n','Disc_Change_1d','Disc_Change_2n','Disc_Change_2d','md1_rev','md2_rev','md3_rev','md4_rev','md5_rev','md6_rev']]
    
    #df_diag_report_pivot4_keys=df_diag_report_pivot4[['vbs_no','WoS_Bucket']]
    df_pivot4_group_agg=df_diag_report_pivot4.groupby(['vbs_no','WoS_Bucket']).sum()
    df_pivot4_group_agg['Wt_MD1_Disc'] = (1 - df_pivot4_group_agg['Wt_MD1_Disc_n']/df_pivot4_group_agg['Wt_MD1_Disc_d'])
    df_pivot4_group_agg['Wt_Curr_Disc'] = (1 - df_pivot4_group_agg['Wt_Curr_Disc_n']/df_pivot4_group_agg['Wt_Curr_Disc_d'])
    df_pivot4_group_agg['Disc_Change'] = (df_pivot4_group_agg['Disc_Change_1n']/df_pivot4_group_agg['Disc_Change_1d'] - df_pivot4_group_agg['Disc_Change_2n']/df_pivot4_group_agg['Disc_Change_2d'])
    #print("df after df_pivot4_group_agg::::::",list(df_pivot4_group_agg))
    df_diag_report_pivot4 = df_pivot4_group_agg[['on_hand_act','Wt_MD1_Disc','Wt_Curr_Disc','Disc_Change','optimization.prcCombinationLevelOutput_0_md1_rev','optimization.prcCombinationLevelOutput_0_md2_rev','optimization.prcCombinationLevelOutput_0_md3_rev','optimization.prcCombinationLevelOutput_0_md4_rev','optimization.prcCombinationLevelOutput_0_md5_rev','optimization.prcCombinationLevelOutput_0_md6_rev','optimization.prcCombinationLevelOutput_0_md7_rev','optimization.prcCombinationLevelOutput_0_md8_rev','optimization.prcCombinationLevelOutput_0_md9_rev','sal_value','optimization.prcCombinationLevelOutput_0_md1_cmd','optimization.prcCombinationLevelOutput_0_md2_cmd','optimization.prcCombinationLevelOutput_0_md3_cmd','optimization.prcCombinationLevelOutput_0_md4_cmd','optimization.prcCombinationLevelOutput_0_md5_cmd','optimization.prcCombinationLevelOutput_0_md6_cmd','optimization.prcCombinationLevelOutput_0_md7_cmd','optimization.prcCombinationLevelOutput_0_md8_cmd','optimization.prcCombinationLevelOutput_0_md9_cmd']]
    #print(df_diag_report_pivot4.head())
    df_diag_report_pivot4_total = df[['vbs_no','on_hand_act','Wt_MD1_Disc_n','Wt_MD1_Disc_d','Wt_Curr_Disc_n','Wt_Curr_Disc_d','Disc_Change_1n','Disc_Change_1d','Disc_Change_2n','Disc_Change_2d','optimization.prcCombinationLevelOutput_0_md1_rev','optimization.prcCombinationLevelOutput_0_md2_rev','optimization.prcCombinationLevelOutput_0_md3_rev','optimization.prcCombinationLevelOutput_0_md4_rev','optimization.prcCombinationLevelOutput_0_md5_rev','optimization.prcCombinationLevelOutput_0_md6_rev','optimization.prcCombinationLevelOutput_0_md7_rev','optimization.prcCombinationLevelOutput_0_md8_rev','optimization.prcCombinationLevelOutput_0_md9_rev','sal_value','optimization.prcCombinationLevelOutput_0_md1_cmd','optimization.prcCombinationLevelOutput_0_md2_cmd','optimization.prcCombinationLevelOutput_0_md3_cmd','optimization.prcCombinationLevelOutput_0_md4_cmd','optimization.prcCombinationLevelOutput_0_md5_cmd','optimization.prcCombinationLevelOutput_0_md6_cmd','optimization.prcCombinationLevelOutput_0_md7_cmd','optimization.prcCombinationLevelOutput_0_md8_cmd','optimization.prcCombinationLevelOutput_0_md9_cmd']]
    
    df_pivot4_total_group_agg=df_diag_report_pivot4_total.groupby(['vbs_no']).sum()
    df_pivot4_total_group_agg['Wt_MD1_Disc'] = (1 - df_pivot4_total_group_agg['Wt_MD1_Disc_n']/df_pivot4_total_group_agg['Wt_MD1_Disc_d'])
    df_pivot4_total_group_agg['Wt_Curr_Disc'] = (1 - df_pivot4_total_group_agg['Wt_Curr_Disc_n']/df_pivot4_total_group_agg['Wt_Curr_Disc_d'])
    df_pivot4_total_group_agg['Disc_Change'] = (df_pivot4_total_group_agg['Disc_Change_1n']/df_pivot4_total_group_agg['Disc_Change_1d'] - df_pivot4_total_group_agg['Disc_Change_2n']/df_pivot4_total_group_agg['Disc_Change_2d'])
    #print("df after df_pivot4_total_group_agg::::::",list(df_pivot4_total_group_agg))
    df_diag_report_pivot4_total = df_pivot4_total_group_agg[['on_hand_act','Wt_MD1_Disc','Wt_Curr_Disc','Disc_Change','optimization.prcCombinationLevelOutput_0_md1_rev','optimization.prcCombinationLevelOutput_0_md2_rev','optimization.prcCombinationLevelOutput_0_md3_rev','optimization.prcCombinationLevelOutput_0_md4_rev','optimization.prcCombinationLevelOutput_0_md5_rev','optimization.prcCombinationLevelOutput_0_md6_rev','optimization.prcCombinationLevelOutput_0_md7_rev','optimization.prcCombinationLevelOutput_0_md8_rev','optimization.prcCombinationLevelOutput_0_md9_rev','sal_value','optimization.prcCombinationLevelOutput_0_md1_cmd','optimization.prcCombinationLevelOutput_0_md2_cmd','optimization.prcCombinationLevelOutput_0_md3_cmd','optimization.prcCombinationLevelOutput_0_md4_cmd','optimization.prcCombinationLevelOutput_0_md5_cmd','optimization.prcCombinationLevelOutput_0_md6_cmd','optimization.prcCombinationLevelOutput_0_md7_cmd','optimization.prcCombinationLevelOutput_0_md8_cmd','optimization.prcCombinationLevelOutput_0_md9_cmd']]
    
    #print("df_pivot4_total_group_agg derived Successfully!!")
    
    df_diag_report_3=df[['vbs_no','On_Hand_ToP_wk']]
    f = {'On_Hand_ToP_wk': [OH_ll,OH_ml]}
    df_diag_report_3_group_agg = df_diag_report_3.groupby('vbs_no').agg(f)
    df_diag_report_3_group_agg.columns=df_diag_report_3_group_agg.columns.map('_'.join)
    df_diag_report_4=df.join(df_diag_report_3_group_agg,on='vbs_no')
    df_diag_report_4['OH_bucket']=df_diag_report_4.apply(deriveOHBucket, axis = 1)
    df_diag_report_4['oh_thresold']=df_diag_report_4.apply(deriveOHThresold, axis = 1)
    
    #print("df_diag_report_4:::::::::",list(df_diag_report_4))
    #print(df_diag_report_4.head())
    
    df_diag_report_disc_OH = df_diag_report_4[['vbs_no','OH_bucket','optimization.currentDiscount']]
    f = {'optimization.currentDiscount': [OH_ll,OH_ml]}
    df_diag_report_disc_OH_group_agg = df_diag_report_disc_OH.groupby(['vbs_no','OH_bucket']).agg(f)
    df_diag_report_disc_OH_group_agg.columns=df_diag_report_disc_OH_group_agg.columns.map('_'.join)
    
    print(df_diag_report_disc_OH_group_agg)
    
    ##refer to _diag_report_initial5 query in hive
    df_diag_report_5=df_diag_report_4.join(df_diag_report_disc_OH_group_agg,on=['vbs_no','OH_bucket'])
    df_diag_report_5['disc_OH_bucket']=df_diag_report_5.apply(deriveDiscOHBucket, axis = 1)
    df_diag_report_5['disc_OH_thresold']=df_diag_report_5.apply(deriveDiscOHThresold, axis = 1)
    
    df_diag_report_5['Wt_Curr_Disc_n']=df_diag_report_5['On_Hand_ToP_wk']*df_diag_report_5['optimization.regularPrice']*(1-df_diag_report_5['optimization.currentDiscount'])
    df_diag_report_5['Wt_Curr_Disc_d']=df_diag_report_5['On_Hand_ToP_wk']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD1_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md1_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md1'].astype(str).astype(int))
    df_diag_report_5['Wt_MD1_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md1_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD2_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md2_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md2'].astype(str).astype(int))
    df_diag_report_5['Wt_MD2_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md2_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD3_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md3_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md3'].astype(str).astype(int))
    df_diag_report_5['Wt_MD3_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md3_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD4_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md4_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md4'].astype(str).astype(int))
    df_diag_report_5['Wt_MD4_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md4_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD5_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md5_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md5'].astype(str).astype(int))
    df_diag_report_5['Wt_MD5_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md5_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD6_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md6_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md6'].astype(str).astype(int))
    df_diag_report_5['Wt_MD6_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md6_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD7_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md7_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md7'].astype(str).astype(int))
    df_diag_report_5['Wt_MD7_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md7_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD8_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md8_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md8'].astype(str).astype(int))
    df_diag_report_5['Wt_MD8_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md8_oh']*df_diag_report_5['optimization.regularPrice']
    df_diag_report_5['Wt_MD9_Disc_n']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md9_oh']*df_diag_report_5['optimization.regularPrice']*(1 - df_diag_report_5['optimization.prcCombinationLevelOutput_0_md9'].astype(str).astype(int))
    df_diag_report_5['Wt_MD9_Disc_d']=df_diag_report_5['optimization.prcCombinationLevelOutput_0_md9_oh']*df_diag_report_5['optimization.regularPrice']
    
    df_diag_report_5_filter = df_diag_report_5[['vbs_no','OH_bucket','disc_OH_bucket','Wt_Curr_Disc_n','Wt_Curr_Disc_d','Wt_MD1_Disc_n','Wt_MD1_Disc_d','Wt_MD2_Disc_n','Wt_MD2_Disc_d','Wt_MD3_Disc_n','Wt_MD3_Disc_d','Wt_MD4_Disc_n','Wt_MD4_Disc_d','Wt_MD5_Disc_n','Wt_MD5_Disc_d','Wt_MD6_Disc_n','Wt_MD6_Disc_d','Wt_MD7_Disc_n','Wt_MD7_Disc_d','Wt_MD8_Disc_n','Wt_MD8_Disc_d','Wt_MD9_Disc_n','Wt_MD9_Disc_d']]
    
  
    df_diag_report_5_group_agg=df_diag_report_5_filter.groupby(['vbs_no','OH_bucket','disc_OH_bucket']).sum()
    df_diag_report_5_group_agg['Wt_Curr_Disc'] = (1 - df_diag_report_5_group_agg['Wt_Curr_Disc_n']/df_diag_report_5_group_agg['Wt_Curr_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD1_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD1_Disc_n']/df_diag_report_5_group_agg['Wt_MD1_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD2_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD2_Disc_n']/df_diag_report_5_group_agg['Wt_MD2_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD3_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD3_Disc_n']/df_diag_report_5_group_agg['Wt_MD3_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD4_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD4_Disc_n']/df_diag_report_5_group_agg['Wt_MD4_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD5_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD5_Disc_n']/df_diag_report_5_group_agg['Wt_MD5_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD6_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD6_Disc_n']/df_diag_report_5_group_agg['Wt_MD6_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD7_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD7_Disc_n']/df_diag_report_5_group_agg['Wt_MD7_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD8_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD8_Disc_n']/df_diag_report_5_group_agg['Wt_MD8_Disc_d'])
    df_diag_report_5_group_agg['Wt_MD9_Disc'] = (1 - df_diag_report_5_group_agg['Wt_MD9_Disc_n']/df_diag_report_5_group_agg['Wt_MD9_Disc_d'])
    print(list(df_diag_report_5_group_agg))
    df_diag_report_5_groupped = df_diag_report_5_group_agg.groupby(['vbs_no','OH_bucket','disc_OH_bucket','Wt_Curr_Disc_n','Wt_Curr_Disc_d','Wt_MD1_Disc_n', 'Wt_MD1_Disc_d', 'Wt_MD2_Disc_n', 'Wt_MD2_Disc_d', 'Wt_MD3_Disc_n', 'Wt_MD3_Disc_d', 'Wt_MD4_Disc_n', 'Wt_MD4_Disc_d', 'Wt_MD5_Disc_n', 'Wt_MD5_Disc_d', 'Wt_MD6_Disc_n', 'Wt_MD6_Disc_d', 'Wt_MD7_Disc_n', 'Wt_MD7_Disc_d', 'Wt_MD8_Disc_n', 'Wt_MD8_Disc_d', 'Wt_MD9_Disc_n', 'Wt_MD9_Disc_d', 'Wt_Curr_Disc', 'Wt_MD1_Disc', 'Wt_MD2_Disc', 'Wt_MD3_Disc', 'Wt_MD4_Disc', 'Wt_MD5_Disc', 'Wt_MD6_Disc', 'Wt_MD7_Disc', 'Wt_MD8_Disc', 'Wt_MD9_Disc'])
    print(list(df_diag_report_5_groupped))
    df_diag_report_oh_chart = pd.DataFrame(df_diag_report_5_groupped.size().reset_index())
    df_diag_report_oh_chart = df_diag_report_oh_chart[['vbs_no','OH_bucket','disc_OH_bucket','Wt_Curr_Disc','Wt_MD1_Disc','Wt_MD2_Disc','Wt_MD3_Disc','Wt_MD4_Disc','Wt_MD5_Disc','Wt_MD6_Disc','Wt_MD7_Disc','Wt_MD8_Disc','Wt_MD9_Disc']]
    df_diag_report_oh_chart = df_diag_report_oh_chart.sort_values(by=['vbs_no','OH_bucket','disc_OH_bucket'])
    
    df_diag_report_5_grouped = df_diag_report_5.groupby(['vbs_no','OH_bucket','disc_OH_bucket','oh_thresold','disc_OH_thresold'])
    df_diag_report_5_reset = pd.DataFrame(df_diag_report_5_grouped.size().reset_index())
    df_diag_report_5_grouped = df_diag_report_5_reset[['vbs_no','OH_bucket','disc_OH_bucket','oh_thresold','disc_OH_thresold']]
    
    writeToExcel(df_1,df_2,df_3,df_diag_report_pivot4,df_diag_report_pivot4_total,df_diag_report_oh_chart,df_diag_report_oh_threshold)
    #writeToExcel(df_1,df_2,df_3,df_diag_report_pivot4,df_diag_report_pivot4_total,df_diag_report_oh_chart)
    
	
    return True
	

def flatten(something,parent_key=None):
	if parent_key==None:
		prefix = ""
	else:
		prefix = parent_key+"_"
	
	if type(something) == type({}):
		temp={}
		for key in something:
			temp.update(flatten(something[key],prefix+key))
		return temp
	elif type(something) == type([]):
		temp = {}
		for index in range(len(something)):
			temp.update(flatten(something[index],prefix+str(index)))
			# temp.update(flatten(something[index],prefix+str(something[index]['id'])))
		return temp
	else:
		return {parent_key:something}


def sometimes_flatten(something, flatten_keys):
	if type(something) == type({}):
		temp={}
		for key in something:
			if key in flatten_keys:
				temp.update(flatten(something[key],key))
			else:
				temp.update({key:sometimes_flatten(something[key],flatten_keys)})
		return temp
	elif type(something) == type([]):
		return [sometimes_flatten(x,flatten_keys) for x in something]
	else:
		return something


def writeToExcel(df_1,df_2,df_3,df_diag_report_pivot4,df_diag_report_pivot4_total,df_diag_report_oh_chart,df_diag_report_oh_threshold):
	writer = pd.ExcelWriter('/tmp/pandas_simple.xlsx', engine='xlsxwriter')
	df_1.to_excel(writer,startrow=0)
	df_1_cnt = df_1.shape[0]+1
	print("df_1_cnt:::::",df_1_cnt)
	
	df_2.to_excel(writer,startrow=df_1_cnt)
	df_2_cnt = df_1_cnt + df_2.shape[0]+1
	print("df_2_cnt:::::",df_2_cnt)
	
	df_3.to_excel(writer,startrow=df_2_cnt)
	df_3_cnt = df_2_cnt + df_3.shape[0]+1
	print("df_3_cnt:::::",df_3_cnt)
	
	df_diag_report_pivot4.to_excel(writer,startrow=df_3_cnt)
	df_diag_report_pivot4_cnt = df_3_cnt + df_diag_report_pivot4.shape[0]+1
	print("df_diag_report_pivot4_cnt:::::",df_diag_report_pivot4_cnt)
	
	df_diag_report_pivot4_total.to_excel(writer,startrow=df_diag_report_pivot4_cnt)
	df_diag_report_pivot4_total_cnt = df_diag_report_pivot4_cnt + df_diag_report_pivot4_total.shape[0]+1
	print("df_diag_report_pivot4_total_cnt:::::",df_diag_report_pivot4_total_cnt)
	
	df_diag_report_oh_chart.to_excel(writer,startrow=df_diag_report_pivot4_total_cnt)
	df_diag_report_oh_chart_cnt = df_diag_report_pivot4_total_cnt + df_diag_report_oh_chart.shape[0]+1
	print("df_diag_report_oh_chart_cnt:::::",df_diag_report_oh_chart_cnt)
	
	df_diag_report_oh_threshold.to_excel(writer,startrow=df_diag_report_oh_chart_cnt)
	df_diag_report_oh_threshold_cnt = df_diag_report_oh_chart_cnt + df_diag_report_oh_threshold.shape[0]+1
	print("df_diag_report_oh_threshold_cnt:::::",df_diag_report_oh_threshold_cnt)
	
	
	writer.save()
	print("Writing to excel done..!! ")
	#localFilename = '/tmp/{}'.format(os.path.basename('pandas_simple.xlsx'))
	#print("localfilename:::::",localFilename)
	s3 = boto3.resource(service_name = 's3')
	s3.meta.client.upload_file(Filename = '/tmp/pandas_simple.xlsx', Bucket = 'entpric-clxprc-sears', Key = '/diagnostic/pandas_simple.xlsx')
	print("SUCCESS: File uploaded to S3 Succesfully.")
	

def storeDFToDB(df):
	try:
		engine = create_engine('mysql+pymysql://' + name + ':' + password +'@' + host_name + '/' + db_name)
		print("Engine:::::::::::::",engine)
		connection = engine.connect()
		#print(df)
		#df.to_sql(name='clearance_kmart_output_final', con=conn, if_exists = 'replace', index=False, index_label=None)
		df.to_sql(con=connection, name='clearance_sears_output_final', if_exists='replace')
		connection.close()
		print("SUCCESS: Written Dataframe to Database Successfully !!")
		#writeToExcel(df)
	except Exception as e:
		print("ERROR: Exception occured while writing Dataframe to Database.")
		raise e
	return True


def deriveCurrentDiscountBucket(df):
    if (df['optimization.currentDiscount'] == 0):
        return '0% to 0%'
    elif (df['optimization.currentDiscount'] > 0) and (df['optimization.currentDiscount'] < 0.1):
        return '1% to 10%'
    elif (df['optimization.currentDiscount'] >= 0.1) and (df['optimization.currentDiscount'] < 0.15):
        return '10% to 15%'
    elif (df['optimization.currentDiscount'] >= 0.15) and (df['optimization.currentDiscount'] < 0.2):
        return '15% to 20%'
    elif (df['optimization.currentDiscount'] >= 0.2) and (df['optimization.currentDiscount'] < 0.25):
        return '20% to 25%'
    elif (df['optimization.currentDiscount'] >= 0.25) and (df['optimization.currentDiscount'] < 0.3):
        return '25% to 30%'
    elif (df['optimization.currentDiscount'] >= 0.3) and (df['optimization.currentDiscount'] < 0.35):
        return '30% to 35%'
    elif (df['optimization.currentDiscount'] >= 0.35) and (df['optimization.currentDiscount'] < 0.4):
    	return '35% to 40%'
    elif (df['optimization.currentDiscount'] >= 0.4) and (df['optimization.currentDiscount'] < 0.45):
        return '40% to 45%'
    elif (df['optimization.currentDiscount'] >= 0.45) and (df['optimization.currentDiscount'] < 0.5):
        return '45% to 50%'
    elif (df['optimization.currentDiscount'] >= 0.5) and (df['optimization.currentDiscount'] < 0.55):
        return '50% to 55%'
    elif (df['optimization.currentDiscount'] >= 0.55) and (df['optimization.currentDiscount'] < 0.6):
        return '55% to 60%'
    elif (df['optimization.currentDiscount'] >= 0.6) and (df['optimization.currentDiscount'] < 0.65):
    	return '60% to 65%'
    elif (df['optimization.currentDiscount'] >= 0.65) and (df['optimization.currentDiscount'] < 0.7):
        return '65% to 70%'
    elif (df['optimization.currentDiscount'] >= 0.7) and (df['optimization.currentDiscount'] < 0.75):
        return '70% to 75%'
    elif (df['optimization.currentDiscount'] >= 0.75) and (df['optimization.currentDiscount'] < 0.8):
        return '75% to 80%'
    elif (df['optimization.currentDiscount'] >= 0.8):
    	return '80% to 100%'



def deriveWOSBucket(df):	
    if (df['On_Hand_ToP_wk']/df['predicted_units'] > 0) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 5):
        return '0 to 5'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 5) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 10):
        return '5 to 10'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 10) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 15):
        return '10 to 15'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 15) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 20):
        return '15 to 20'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 20) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 25):
        return '20 to 25'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 25) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 30):
        return '25 to 30'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 30) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 40):
        return '30 to 40'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 40) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 50):
    	return '40 to 50'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 50) and (df['On_Hand_ToP_wk']/df['predicted_units'] <= 100):
        return '50 to 100'
    elif (df['On_Hand_ToP_wk']/df['predicted_units'] > 100):
    	return '100 & above'
    

def deriveOHBucket(df):
	if (df['On_Hand_ToP_wk']<=df['On_Hand_ToP_wk_OH_ll']):
	    return 'Low'
	elif (df['On_Hand_ToP_wk']<=df['On_Hand_ToP_wk_OH_ml'] and df['On_Hand_ToP_wk']>df['On_Hand_ToP_wk_OH_ll']):
	    return 'Medium'
	elif (df['On_Hand_ToP_wk']>df['On_Hand_ToP_wk_OH_ml']):
	    return 'High'
		
def deriveOHThresold(df):
    if (df['On_Hand_ToP_wk']<=df['On_Hand_ToP_wk_OH_ll']):
        return "<="+str(round(df['On_Hand_ToP_wk_OH_ll']))
    elif (df['On_Hand_ToP_wk']<=df['On_Hand_ToP_wk_OH_ml'] and
    df['On_Hand_ToP_wk']>df['On_Hand_ToP_wk_OH_ll']):
        return str(round(df['On_Hand_ToP_wk_OH_ll']))+" to "+str(round(df['On_Hand_ToP_wk_OH_ml']))
    elif (df['On_Hand_ToP_wk']>df['On_Hand_ToP_wk_OH_ml']):
        return ">"+str(round(df['On_Hand_ToP_wk_OH_ml']))

def deriveDiscOHBucket(df):
	if (df['optimization.currentDiscount']<=df['optimization.currentDiscount_OH_ll']):
	    return 'Low'
	elif (df['optimization.currentDiscount']<=df['optimization.currentDiscount_OH_ml'] and df['optimization.currentDiscount']>df['optimization.currentDiscount_OH_ll']):
	    return 'Medium'
	elif (df['optimization.currentDiscount']>df['optimization.currentDiscount_OH_ml']):
	    return 'High'
# case when d.current_disc <= d.disc_OH_ll then concat("<=", cast(round(d.disc_OH_ll*100) as string),"%")
#280 when d.current_disc <= d.disc_OH_ml and d.current_disc > d.disc_OH_ll then concat( cast(round(d.disc_OH_ll*100) as string),"%", " to ", cast(round(d.disc_OH_ml*100)     as string),"%")
		
def deriveDiscOHThresold(df):
    if (df['optimization.currentDiscount']<=df['optimization.currentDiscount_OH_ll']):
        return "<="+str(round(df['On_Hand_ToP_wk_OH_ll']))+"%"
    elif (df['optimization.currentDiscount']<=df['optimization.currentDiscount_OH_ml'] and
    df['optimization.currentDiscount']>df['optimization.currentDiscount_OH_ll']):
        return str(round(df['optimization.currentDiscount_OH_ll']))+"% to "+str(round(df['optimization.currentDiscount_OH_ml']))+"%"
    elif (df['optimization.currentDiscount']>df['optimization.currentDiscount_OH_ml']):
        return ">"+str(round(df['optimization.currentDiscount_OH_ml']))+"%"


def deriveMD1CombinationsAndAggregate(df,prefix,groupbyCol1,groupbyCol2,startIndex):
	filterColumns=[]
	i=0
	for x in range(10,100,5):
	    key="MD1_"+str(x)
	    #print("key:::::::::",key)
	    df[key] = np.where(df['optimization.prcCombinationLevelOutput_0_md1'].astype(str).astype(int)==x, prefix, 0)
	    filterColumns.append(key)
	df_filter=df[[groupbyCol1,groupbyCol2,filterColumns[0],filterColumns[1],filterColumns[2],filterColumns[3],filterColumns[4],filterColumns[5],filterColumns[6],filterColumns[7],filterColumns[8],filterColumns[9],filterColumns[10],filterColumns[11],filterColumns[12],filterColumns[13],filterColumns[14],filterColumns[15],filterColumns[16],filterColumns[17]]]
	#print(df_filter)
	df_group_by_agg=df_filter.groupby([groupbyCol1,groupbyCol2]).sum()
	print(df_group_by_agg)
	#writeToExcel(df_group_by_agg,startIndex)
	return df_group_by_agg

def OH_ll(x):
    return x.quantile(0.33)

def OH_ml(x):
    return x.quantile(0.66)