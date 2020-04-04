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
            print("bucket Name:::::",bucket.name)
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
    print("jsonObj decoded Successfully!!")
    
    # Step 2 - Flatten the JSON object such that it could be easily converted to a pandas Dataframe
    flatten_keys = ['prcCombinationLevelOutput']
    a = sometimes_flatten(jsonObj,flatten_keys)
    print("sometimes_flatten invoked Successfully!!")
    
    # Step 3 - Convert Flatten JSON obj to Dataframe
    df = pd.DataFrame.from_dict(json_normalize(a), orient='columns')
    print("Flattened JSON obj to Dataframe Successfully!!")
    
    # Step 4 - Store the dataframe to Aurora DB
    #b = storeDFToDB(df)
    #print("storeDFToDB invoked Successfully!!")
    
    # Step 5 - Derive additional fields required for reporting from the original dataframe    
    df['Current_Disc_Bucket'] = df.apply(deriveCurrentDiscountBucket, axis = 1)
    #print("df[Current_Disc_Bucket]::::::",df['Current_Disc_Bucket'])
    print("df[Current_Disc_Bucket] derived Successfully!!")
    
    df['WoS_Bucket'] = df.apply(deriveWOSBucket, axis = 1)
    #print("df['WoS_Bucket']:::::",df['WoS_Bucket'])
    print("df[WoS_Bucket] derived Successfully!!")
    
    
    df['MD1_10'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.10, 1, 0)
    df['MD1_15'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.15, 1, 0)
    df['MD1_20'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.20, 1, 0)
    df['MD1_25'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.25, 1, 0)
    df['MD1_30'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.30, 1, 0)
    df['MD1_35'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.35, 1, 0)
    df['MD1_40'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.40, 1, 0)
    df['MD1_45'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.45, 1, 0)
    df['MD1_50'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.50, 1, 0)
    df['MD1_55'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.55, 1, 0)
    df['MD1_60'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.60, 1, 0)
    df['MD1_65'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.65, 1, 0)
    df['MD1_70'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.70, 1, 0)
    df['MD1_75'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.75, 1, 0)
    df['MD1_80'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.80, 1, 0)
    df['MD1_85'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.85, 1, 0)
    df['MD1_90'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.90, 1, 0)
    df['MD1_95'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.95, 1, 0)
    
    #print("df after derivation of MD1::::::::::::",df)
    print("MD1 derived Successfully!!")
    
    df['OH_ll'] = np.percentile(df['On_Hand_ToP_wk'],0.33)
    print("OH_ll derived Successfully!!")
    '''df['MD1_10'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.10, md1_units, 0)
    df['MD1_15'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.15, md1_units, 0)
    df['MD1_20'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.20, md1_units, 0)
    df['MD1_25'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.25, md1_units, 0)
    df['MD1_30'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.30, md1_units, 0)
    df['MD1_35'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.35, md1_units, 0)
    df['MD1_40'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.40, md1_units, 0)
    df['MD1_45'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.45, md1_units, 0)
    df['MD1_50'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.50, md1_units, 0)
    df['MD1_55'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.55, md1_units, 0)
    df['MD1_60'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.60, md1_units, 0)
    df['MD1_65'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.65, md1_units, 0)
    df['MD1_70'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.70, md1_units, 0)
    df['MD1_75'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.75, md1_units, 0)
    df['MD1_80'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.80, md1_units, 0)
    df['MD1_85'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.85, md1_units, 0)
    df['MD1_90'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.90, md1_units, 0)
    df['MD1_95'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.95, md1_units, 0)
	
	print("MD1 units derived Successfully!!")

	df['MD1_10'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.10,  inventory_MD1, 0)
    df['MD1_15'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.15,  inventory_MD1, 0)
    df['MD1_20'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.20,  inventory_MD1, 0)
    df['MD1_25'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.25,  inventory_MD1, 0)
    df['MD1_30'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.30,  inventory_MD1, 0)
    df['MD1_35'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.35,  inventory_MD1, 0)
    df['MD1_40'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.40,  inventory_MD1, 0)
    df['MD1_45'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.45,  inventory_MD1, 0)
    df['MD1_50'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.50,  inventory_MD1, 0)
    df['MD1_55'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.55,  inventory_MD1, 0)
    df['MD1_60'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.60,  inventory_MD1, 0)
    df['MD1_65'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.65,  inventory_MD1, 0)
    df['MD1_70'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.70,  inventory_MD1, 0)
    df['MD1_75'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.75,  inventory_MD1, 0)
    df['MD1_80'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.80,  inventory_MD1, 0)
    df['MD1_85'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.85,  inventory_MD1, 0)
    df['MD1_90'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.90,  inventory_MD1, 0)
    df['MD1_95'] = np.where(df['optimization.prcCombinationLevelOutput_0_md1']==0.95,  inventory_MD1, 0)
	
	print("Inventory MD1 derived Successfully!!")
	
	df['Wt_MD1_Disc'] = (1 - (df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice']*(1-df['optimization.prcCombinationLevelOutput_0_md1'])))/(df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice'])
	print("Wt_MD1_Disc derived successfully.")
	
	df['Wt_Curr_Disc'] = (1 - df['On_Hand_ToP_wk']*df['optimization.regularPrice']*(1-df['optimization.currentDiscount'])) / (df['On_Hand_ToP_wk']*df['optimization.regularPrice'])
	print("Wt_Curr_Disc derived successfully.")
	
	df['Disc_Change'] = (df['On_Hand_ToP_wk']*df['optimization.regularPrice']*(1-df['optimization.currentDiscount'])) / ((df['On_Hand_ToP_wk']*df['optimization.regularPrice']) - (df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice']*(1-df['optimization.prcCombinationLevelOutput_0_md1'])) / (df['optimization.prcCombinationLevelOutput_0_md1_oh']*df['optimization.regularPrice'])) 
	print("Disc_Change derived successfully.")
	
	df['OH_ll'] = np.percentile(df['On_Hand_ToP_wk'],0.33)
	print("OH_ll derived Successfully!!")
	
	df['OH_ml'] = np.percentile(df['On_Hand_ToP_wk'],0.66)
	print("OH_ml ::::: ",OH_ml)
	
	df['OH_bucket'] = df.apply(deriveOH_bucket, axis = 1)
	#df['oh_thresold'] = ?
	
	df['disc_OH_bucket'] = df.apply(deriveDisc_OH_bucket, axis = 1) 
	#df['disc_OH_thresold'] = ?'''
	


	
    #Split the original dataframe to two parts Initial & Subsequent once all the required columns are derived
    #df_initial=df.filter(['clearance_flag'==0])
    #df_sub=df.filter(['clearance_flag'==1])
    
    # Step 6 - Apply groupby on the requi
    # red columns are create a subset df
    #curr_disc_buck_df_initial = df_initial.groupby(['div_no','currentDiscount_Bucket'])
    
    # Step 7 - Apply aggregations on the subseted dataframe
    #curr_disc_buck_df_initial['md1_10'].agg(np.sum)
    
    # Step 8 - Write all the subseted dataframes to Excel and store it to S3 bucket
    #writeToExcel(curr_disc_buck_df_initial,0)
    #writeToExcel(curr_disc_buck_df_sub,0)
    #writeToExcel(wos_buck_df_initial,18)
    #writeToExcel(wos_buck_df_sub,18)
    c = writeToExcel(df)
	
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


def writeToExcel(df):
	df.to_excel('/tmp/pandas_simple.xlsx')
	print("Writing to excel done..!! ")
	localFilename = '/tmp/{}'.format(os.path.basename('pandas_simple.xlsx'))
	print("localfilename:::::",localFilename)
	s3 = boto3.resource(service_name = 's3')
	s3.meta.client.upload_file(Filename = '/tmp/pandas_simple.xlsx', Bucket = 'entpric-clx-sears', Key = '/diagnostic/pandas_simple.xlsx')
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
    

def deriveOH_bucket(df):
    if (df['On_Hand_ToP_wk'] <= df['OH_ll']):
        return 'Low'
    elif (df['On_Hand_ToP_wk'] <= df['OH_ml']):
        return 'Medium'
    elif (df['On_Hand_ToP_wk'] > df['OH_ml']):
        return 'High'


def deriveDisc_OH_bucket(df):
    if (df['optimization.currentDiscount'] <= df['disc_OH_ll']):
        return 'Low'
    elif (df['optimization.currentDiscount'] <= df['disc_OH_ml']) and (df['optimization.currentDiscount'] > df['disc_OH_ll']):
        return 'Medium'
    elif (df['optimization.currentDiscount'] > df['disc_OH_ml']):
        return 'High'

