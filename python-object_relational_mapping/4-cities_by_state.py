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

# Execute the query to select cities from the database
query = '''
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        '''
cursor.execute(query)

# Fetch all rows from the result set
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()