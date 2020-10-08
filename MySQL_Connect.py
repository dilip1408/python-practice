# ##-- MySQL Connection -- ###
# import mysql.connector as mc
#
# mydb=mc.connect(host="spaceplanning.cluster-cenwssqguqtm.us-east-2.rds.amazonaws.com", port="3306",user="dvoruga",passwd="prl9WufUvEg5", database="Spaceman")
#
# mycursor=mydb.cursor()
# mycursor.execute("SELECT * FROM spaceman.days_to_check limit 2")
# result = mycursor.fetchall()
#
# for i in result:
#     print(i)
###-- MySQL Connection END-- ###

# from sqlalchemy import create_engine
# engine = create_engine('mysql+pymysql://', +name)
import sqlalchemy as db
from sqlalchemy.engine import create_engine
from sqlalchemy.sql import select
name="dvoruga"
password="prl9WufUvEg5"
host_name = "spaceplanning.cluster-cenwssqguqtm.us-east-2.rds.amazonaws.com"
db_name = "Spaceman"
#engine_live = sqlalchemy.create_engine('mysql+pymysql://:@spaceplanning.cluster-cenwssqguqtm.us-east-2.rds.amazonaws.com/Spaceman' )
engine = create_engine('mysql+pymysql://' + name + ':' + password +'@' + host_name + '/' + db_name)
#engine = create_engine('mysql+pymysql://' + name + ':' + password +'@' + host_name + '/' + db_name)
connection_live = engine.connect()
# simple select
print("\n -- SIMPLE SELECT -- ")

# s = select([chk_item])
# result = connection_live.execute(s)
metadata = db.MetaData()
census = db.Table('chk_item', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())


# loop through results

# for r in result:
#   print(result)
print(connection_live.close())