import mysql.connector
import os

connector = mysql.connector.connect(
  host="db",
  user="root",
  password=os.environ['MYSQL_ROOT_PASSWORD']
)

def insert(sql,value=None):
  mycursor = connector.cursor()
  if(value is None):
    mycursor.execute(sql)
  else:
    mycursor.execute(sql,value)
  connector.commit()
  print(mycursor.rowcount,"record inserted")