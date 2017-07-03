import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE observations (timest timestamp,date_of_observation date,  oneviewid INT, shift TEXT, department TEXT, area TEXT, employee_exam TEXT, \
 activity TEXT, attention_work TEXT, attention_road TEXT, appropriate_tools TEXT, tools_is_ok TEXT, ppe TEXT, capture TEXT, comment TEXT)')
print ("Table created successfully")
conn.close()