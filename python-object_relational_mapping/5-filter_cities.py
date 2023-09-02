#!/usr/bin/python3
import MySQLdb
import sys

# Get MySQL connection parameters and state name from command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                     passwd=mysql_password, db=database_name)

# Create a cursor object to execute queries
cursor = db.cursor()

# Execute the query to select cities of the given state
query = '''
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        '''
cursor.execute(query, (state_name,))

# Fetch all rows from the result set
results = cursor.fetchall()

# Extract the city names from the result set
cities = [row[0] for row in results]

# Display the results
if cities:
    print(', '.join(cities))
else:
    print("No cities found for the given state.")

# Close the cursor and database connection
cursor.close()
db.close()