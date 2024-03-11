import sqlite3

# Create a connection to the database
conn = sqlite3.connect('telemedicine.db')

# Create a cursor object
c = conn.cursor()

# Now you can use the cursor object to execute SQLite commands

# Don't forget to close the connection when you're done
conn.close()
