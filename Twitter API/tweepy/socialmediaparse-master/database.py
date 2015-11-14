import MySQLdb
import mysql.connector

def main():
	cnx = mysql.connector.connect(user='root', password='root', database='tweettable')
	cursor = cnx.cursor(buffered=True)

	query = ("SELECT tweet FROM taula4bitDefault WHERE 1")

	cursor.execute(query)

	numrows = cursor.rowcount
	print "numrows = ", numrows

	#Get and display the rows one at a time
	for i in cursor:
		print i

	cursor.close()
	cnx.close()

main()

# def main():

#   # Connect to the MySQL database
#   db = MySQLdb.connect("localhost","root","root","tweettable" )

#   # Creation of a cursor
#   cursor = db.cursor()

#   # Execution of a SQL statement
#   cursor.execute ("SELECT * FROM  taula4bitDefault WHERE 1")

#   # Get the total number of rows
#   numrows = int (cursor.rowcount)
#   print "numrows = ", numrows

#   # Get and display the rows one at a time
#   for i in range (numrows):
#     row = cursor.fetchone()
#     if (row):
#       print row[0], row[1], row[2]

#   # Close the cursor
#   cursor.close()

# main()
		

