import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mayafit23!"
)

mycursor = mydb.cursor()
mycursor.execute("use coin")

mycursor.execute("SELECT * FROM stories")

myresult = mycursor.fetchall()

list = []

for item in myresult:
    dict = {}
    dict['title'] = item[1]
    dict['source'] = item[2]
    dict['body'] = item[3]
    dict['image_url'] = item[4]
    list.append(dict)

print(json.dumps(list))