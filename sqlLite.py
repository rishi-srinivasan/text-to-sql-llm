import sqlite3

# connect to sqlLite
conn = sqlite3.connect('student.db')

# create a cursor object to insert record and create table
cursor = conn.cursor()

# create table
table_info="""
CREATE TABLE IF NOT EXISTS STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# insert records
cursor.execute('''INSERT INTO STUDENT VALUES ('Rishi','Cloud Computing','A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Nicolas','Data Science','E')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Alex','Project Management','B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Marc','Generative AI','D')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Yash','Cloud Computing','A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Felix','Python','C')''')

# display records
print("Inserted records are: ")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# commit and close sql connection
conn.commit()
conn.close()
