#!/usr/bin/python3
import MySQLdb
import sys

# Get MySQL connection parameters from command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                     passwd=mysql_password, db=database_name)

# Create a cursor object to execute queries
cursor = db.cursor()

# Execute the query to select states starting with 'N'
query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
cursor.execute(query)

# Fetch all rows from the result set
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()