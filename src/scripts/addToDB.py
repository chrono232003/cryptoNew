import mysql.connector

import requests
import json
from datetime import datetime
from datestr import Date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mayafit23!"
)

x = requests.get('https://min-api.cryptocompare.com/data/v2/news/')
y = json.loads(x.content)
z = y["Data"]

t = datetime.date(datetime.now())

mycursor = mydb.cursor()
mycursor.execute("use coin")
#myresult = mycursor.fetchall()

for item in z:
    # escape apostrophes
    title = json.dumps(item['title'])
    body = json.dumps(item['body'])
    source = json.dumps(item['source'])
    image_url = json.dumps(item['imageurl'])

    #print("INSERT INTO stories (title, source, body, image_url, date) VALUES('" + title + "','" + source + "','" + body + "','" + image_url + "','" + t.strftime('%Y-%m-%d') + "')")
    mycursor.execute("INSERT INTO stories (title, source, body, image_url, date) VALUES(" + title + "," + source + "," + body + "," + image_url + ",'" + t.strftime('%Y-%m-%d') + "')")

    mydb.commit()