#Importing the libraries
import sqlite3 as sql
from flask import Flask,render_template,request,redirect,url_for,flash

app=Flask(__name__)
app.secret_key='admin123'

#Creating a database and connecting to the database
@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("student.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    #Viewing the details for the student table 
    cur.execute("select * from student")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

#Adding the details of the student 
@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        dob=request.form['dob']
        amount_due=request.form['amount_due']
        con=sql.connect("student.db")
        cur=con.cursor()
        cur.execute("insert into student(first_name,last_name,dob,amount_due) values (?,?,?,?)",(first_name,last_name,dob,amount_due))
        con.commit()
        flash('Student Added','success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

#Editing the details of the student
@app.route("/edit_user/<string:student_id>",methods=['POST','GET'])
def edit_user(student_id):
    if request.method=='POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        dob=request.form['dob']
        amount_due=request.form['amount_due']
        con=sql.connect("student.db")
        cur=con.cursor()
        cur.execute("update student set first_name=?,last_name=?,dob=?,amount_due=? where student_id=?",(first_name,last_name,dob,amount_due,student_id))
        con.commit()
        flash('Student Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("student.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from student where student_id=?",(student_id,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)

#Deleting the details of a particular student
@app.route("/delete_user/<string:student_id>",methods=['GET'])
def delete_user(student_id):
    con=sql.connect("student.db")
    cur=con.cursor()
    cur.execute("delete from student where student_id=?",(student_id,))
    con.commit()
    flash('User Deleted','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.run()
