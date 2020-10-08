# # from google.cloud import bigquery
# # client = bigquery.Client()
# #
# #
# # import os
# # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/dvoruga/Downloads/shc-dfs-test-78d7a2e8ed52.json"
# #
# # # static_df = pd.read_gbq(static_query, env['BILLING_PROJECT'], dialect='legacy')
# #
# # Perform a query.
# # QUERY = ('SELECT Table_name FROM shc-dfs-test.dfs_test.backup_master')
# # query_job = client.query(QUERY)  # API request
# # rows = query_job.result()  # Waits for query to finish
# # #
# # for row in rows:
# #     print(row.name)
# 
from google.cloud import bigquery
# # from airflow.contrib.hooks.bigquery_hook import BigQueryHook
# # from bigquery_run_with_timeout_retry.run_bigquery import read_gbq, to_gbq
# # from bigquery_run_with_timeout_retry.run_bigquery import runbq
#
# # Construct a BigQuery client object.
client = bigquery.Client.from_service_account_json('C:/Users/dvoruga/Downloads/shc-dfs-test-78d7a2e8ed52.json')
import pandas as pd
# #
# # query = """
# #        SELECT * FROM shc-dfs-test.dfs_test.backup_master limit 10;
# #     """
# # query_job = client.query(query) # Make an API request.
# # df=read_gbq(query)
# # print(df)
# # for row in query_job:
# #      print(type(row))
#
#
def comparing_tables():
    import pandas as pd
    pd.set_option('display.max_columns', 15)
    pd.set_option('display.precision',16)
    all_tables = pd.read_csv('C:/Users/dvoruga/Downloads/All_tables.csv')
    master_comparision = pd.read_csv('C:/Users/dvoruga/Downloads/master_comparision.csv')
    # query_all_tables = 'SELECT *,TIMESTAMP_MILLIS(creation_time) as create_ts, TIMESTAMP_MILLIS(last_modified_time) as modified_ts FROM `shc-dfs-test.dfs_tbl_bkp.__TABLES__` where row_count between 1 and 5 order by modified_ts desc'
    # # logging.info('Executing: %s', str(qry))
    # all_tables = client.query(query_all_tables)
    all_tables = all_tables[['dataset_id','table_id','modified_ts']]
    # all_tables['modified_ts'].astype(int)
    # all_tables['modified_ts'].astype(int)
    # query_master_comparision = '''select dataset_id, table_id, modified_ts from shc-dfs-test.dfs_test.backup_master'''
    # master_comparision = client.query(query_master_comparision)
    master_comparision = master_comparision[['dataset_id','table_id','modified_ts']]
    # master_comparision['modified_ts'].astype(int)
    merged_df = all_tables.merge(master_comparision, how='outer', indicator='ADD_MOD_DROP', on=['table_id','dataset_id'])


    merged_df = merged_df.replace({'right_only': 'Drop', 'left_only': 'Add', 'both': 'Exist'})
    print(merged_df)
    # # exist_tables = merged_df.loc[merged_df['ADD_MOD_DROP'] == 'Exist']
    # # not_modified = pd.concat([exist_tables['modified_ts_x'], exist_tables['modified_ts_y']], axis=1)
    # # exp = graph.loc[(graph['wk_no'] == top_wk), ['OFR_ID','exp','std_units','ini_pro']]

    newly_added = merged_df[merged_df['ADD_MOD_DROP'] == 'Add']
    dropped  = merged_df[merged_df['ADD_MOD_DROP'] == 'Drop']
    modified = merged_df.loc[(merged_df['ADD_MOD_DROP'] == 'Exist') & (merged_df['modified_ts_x'] != merged_df['modified_ts_y'])]
    modified = modified.replace({'Exist':'Modified'})
    # modified.loc[modified['ADD_MOD_DROP']] = 'Modified'
    # modified.loc[modified.ADD_MOD_DROP:],'ADD_MOD_DROP'] = modified.apply(lambda x: x['ADD_MOD_DROP'].replace('Exist','Modified'), axis=1)
    # modified['ADD_MOD_DROP']= modified.loc[modified.ADD_MOD_DROP == 'Exist','ADD_MOD_DROP'] = 'Modified' #This is returning a warning - returning-a-view-versus-a-copy
    print("modified::::::\n", modified)


    not_modified = merged_df.loc[(merged_df['ADD_MOD_DROP'] == 'Exist') & (merged_df['modified_ts_x'] == merged_df['modified_ts_y'])]
    not_modified = not_modified.replace({'Exist': 'Not_Modified'})
    # not_modified['ADD_MOD_DROP'] = not_modified.apply(lambda x: x['ADD_MOD_DROP'].replace('Exist','Not_Modified'),axis =1) #This is returning a warning - SettingWithCopyWarning
    print("Not_Modified:::\n", not_modified)
    # # df8 = df7[df7['State'] == df7['STATE_ALPHA']]
    # # exist_tables['is_winner'] = exist_tables['modified_ts_x'].str.lower() == exist_tables['modified_ts_y'].str.lower()
    #
    # # exist_tables['result'] = exist_tables.loc[exist_tables['modified_ts_x'] == exist_tables['modified_ts_x'], 'no_change', 'changed']
    # return newly_added, dropped, modified, not_modified
    print("Dropped:::\n",dropped)
    print("modified::::\n",modified)

comparing_tables()

# bqclient = bigquery.Client()
# query_string =
# dataframe = (
#     bqclient.query(query_string)
#     .result()
#     .to_dataframe(bqstorage_client=bqstorageclient)
# )
# print(dataframe.head())
# bq = BigQueryHook(bigquery_conn_id='bigquery_default', delegate_to=None, use_legacy_sql=False, location='US')
# cEYW_tbls = bq.get_pandas_df(qry)




#     insert_gbq = pd.concat([newly_added,modified,not_modified,dropped], join='outer')
#     insert_gbq = insert_gbq.reset_index(drop=True)
#     print("create_table_list:::::\n",insert_gbq)
#     insert_gbq = insert_gbq[['dataset_id_x','table_id','modified_ts_x','ADD_MOD_DROP']]
#     print("insert into temp bgq table to be pickup in the next task:::::\n",insert_gbq)
#     insert_gbq.to_gbq('dfs_test.archival_extracted_data_temp', project_id='shc-dfs-test', chunksize=None, reauth=False,
#                       if_exists='replace',
#                       table_schema=[{'name': 'dataset_id_x', 'type': 'STRING'}, {'name': 'table_id', 'type': 'STRING'},
#                                     {'name': 'modified_ts_x', 'type': 'INTEGER'},
#                                     {'name': 'ADD_MOD_DROP', 'type': 'STRING'}])


# pd.set_option('display.max_columns',10)
# sql ='''select dataset_id_x, table_id, modified_ts_x, ADD_MOD_DROP from dfs_test.archival_extracted_data_temp'''
# project_id = 'shc-dfs-test'
# create_table_list = pd.read_gbq(sql, project_id=project_id, dialect='standard')
# print(create_table_list.dtypes)
# create_table_list = create_table_list.loc[(create_table_list['ADD_MOD_DROP'] == 'Add') | (create_table_list['ADD_MOD_DROP'] == 'Modified')]
# # create_table_list['dataset_id_x'].astype(str)
# # create_table_list['table_id'].astype(str)
# # create_table_list['modified_ts_x'].astype(np.int64)
# # create_table_list['ADD_MOD_DROP'].astype(str)
# print(create_table_list)

# table_list = []
# query = []
# for i in range(0, create_table_list.shape[0]):
#     table_list.append([create_table_list.iloc[i, 0], create_table_list.iloc[i, 1], str(int(create_table_list.iloc[i, 2]))])
#     query.append("insert into dfs_test.backup_master values('" + create_table_list.iloc[i, 0] + "','"+ create_table_list.iloc[i, 1] + "'," +str(int(create_table_list.iloc[i, 2])) +")")
# print(query)
# print("table_list:::::::::",table_list)
# #lv_bq_project #This need to be replaced with actual bq project
# for i, rec in enumerate(table_list):
#     ds = rec[0]
#     tab = rec[1]
#     ms = rec[2]
#     ms = str(int(ms))
#     tgt_tab = project_id + ds + '_' + tab
#     src_table = project_id + '.' + ds+ '.' +tab
#     tgt_table = project_id + ds+ '_' +tab+ '_' +ms
#     print("src_table:::\n",src_table)
#     print("tgt_table:::\n",tgt_table)
#
#
# task_list.append(BigQueryToBigQueryOperator(
#         task_id='backup_' + tab,
#         source_project_dataset_tables=src_table,
#         destination_project_dataset_table=tgt_table,
#         create_disposition='CREATE_IF_NEEDED',
#         write_disposition='WRITE_TRUNCATE',
#         dag=dag)
# master_rows_remove = pd.concat([dropped, modified])  # insert/delete a row into master table
# print("master_rows_remove", master_rows_remove[['dataset_id_y', 'table_id', 'modified_ts_y']])
#
# q = SELECT dataset_id_x,table_id,modified_ts_x FROM `shc-dfs-test.dfs_test.archival_extracted_data_temp` group by 1,2,3;
# bq = BigQueryHook(bigquery_conn_id='bigquery_default', delegate_to=None, use_legacy_sql=False, location='US')
#     cEYW_tbls = bq.get_pandas_df(q)

#This is not working as the destination table structure is different.
# create_table_list.to_gbq('dfs_test.backup_master', project_id='shc-dfs-test', chunksize=None, reauth=False,
#                   if_exists='append',
# )

# client.insert_rows_from_dataframe(dataframe='create_table_list',table = )
# client.insert_rows_from_dataframe('shc-dfs-test.dfs_test.backup_master', 'create_table_list', selected_fields=None, chunk_size=500)
    # for q in query:
    #     client.query(q)


    #     query_job = client.query(q)
    #     for job in query_job:
    #         print(job)







        # for table in table_list:
    #     table[2].astype(int)
    #     print(type(table[2]))
    # table_list1 = '.'.join(table_list)
    # print(table_list1)
    # for column in create_table_list[['dataset_id_x','table_id','modified_ts_x']]:
    #     column_series = create_table_list[column]
    #     print("Row:::",column_series)
    #     print("Row contents::::",column_series.values)
    # print(dropped)
    # print(modified)
    # print(not_modified)

# comparing_tables()

# def table_dump():
#     dropped = comparing_tables()
#     print(dropped)
#     for e in dropped:
#         print(e)
#
# table_dump()

#
# # dropped_df = merged_df.loc[((merged_df['ADD_MOD_DROP'] == 'Drop')]
# # merged_df = pd.merge(all_tables,master_comparision, how='outer',left_on='table_id',right_on='Table_name')
# # print(exist_tables)

# print("test")

from itertools import permutations

# username = ["sandyb@","sbrown@"]
# domain =["gmail","yahoo"]
# suffixes = [".com",".net"]
#
# z = zip(username,domain)
# username.extend(domain)
# username.extend(suffixes)
# print(list(z))
# # no length entered so default length
# # taken as 4(the length of string GeEK)
# p = permutations([username,domain,suffixes],1)
#
# # Print the obtained permutations
# for j in list(p):
#     print(j)

# def recurse(username, domain,suffixes):
#     return recurse(username + domain + suffixes)
#
# print(recurse([username, domain,suffixes]))