import sqlite3 as sql

#connecting to the database
con = sql.connect('student.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS student")
#Creating a table here
sql ='''CREATE TABLE "student" (
	"student_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT,
	"last_name"	TEXT,
    "dob"	TEXT,
    "amount_due"	TEXT
)'''
cur.execute(sql)
con.commit()
con.close()
