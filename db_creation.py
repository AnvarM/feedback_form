import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE feedback (feedback_title TEXT,feedback_date DATE,name TEXT, department TEXT,question1 TEXT,question2 TEXT,question3 TEXT,comment TEXT)')
print ("Table created successfully")
conn.close()