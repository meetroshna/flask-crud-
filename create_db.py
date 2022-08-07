import sqlite3 as sql

#connect to SQLite
con = sql.connect('student.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS student")

#Create users table  in db_web database
sql ='''CREATE TABLE "student" (
	"student_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT,
	"last_name"	TEXT,
    "dob"	TEXT,
    "amount_due"	TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()