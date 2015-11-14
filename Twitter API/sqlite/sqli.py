import sqlite3
conn = sqlite3.connect('pythontweet.db')
c = conn.cursor()

def tableCreate():
	c.execute("CREATE TABLE top200R (time VARCHAR(20), username VARCHAR(20), tweet VARCHAR(200) )")
