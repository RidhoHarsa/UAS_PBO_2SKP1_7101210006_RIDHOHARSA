host = "localhost"
user = "root"
passwd = "ri15"

import mysql.connector as mysql
import os

db = mysql.connect(
  host = host,
  user = user,
  passwd = passwd
  
)
cursor= db.cursor()
cursor.execute("CREATE DATABASE uas_oop_7101210006_RidhoHarsa")
cursor.execute("SHOW DATABASES")
data = cursor.fetchall()
print(data)