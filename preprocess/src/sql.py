import mysql.connector
import os

connector = mysql.connector.connect(
  host="bia.raknatee.dev",
  # host="db",
  user="root",
  password=os.environ['MYSQL_ROOT_PASSWORD'],
  database = "bia_data"
)

def insert(sql,p=False):
  mycursor = connector.cursor()
  mycursor.execute(sql)
  connector.commit()
  if(p):
    print(mycursor.rowcount,"record inserted")