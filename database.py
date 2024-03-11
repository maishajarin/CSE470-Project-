import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# You can now interact with the database using the `conn` object

# Don't forget to close the connection when you're done
conn.close()

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('telemedicine.db')

# Create a cursor object
c = conn.cursor()

# Create table for Users
c.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('Patient', 'Doctor', 'Admin'))
    )
''')

# Create table for Doctors (if you need to store additional information about doctors)
c.execute('''
    CREATE TABLE Doctors (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL UNIQUE,
        specialization TEXT,
        location TEXT,
        availability TEXT,
        FOREIGN KEY(user_id) REFERENCES Users(id)
    )
''')

# Create table for Appointments
c.execute('''
    CREATE TABLE Appointments (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        doctor_id INTEGER NOT NULL,
        appointment_time TEXT NOT NULL,
        FOREIGN KEY(patient_id) REFERENCES Users(id),
        FOREIGN KEY(doctor_id) REFERENCES Doctors(id)
    )
''')

# Save (commit) the changes and close the connection
conn.commit()
conn.close()

