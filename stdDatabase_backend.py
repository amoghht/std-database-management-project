#backend
import sqlite3
import tkinter.messagebox as mbox

def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student4(StdID text,Firstname text,Lastname text,"
                "Dob text,Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()

def addstudentrecord(StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile):
    con = sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("INSERT INTO student4 VALUES (?,?,?,?,?,?,?,?)",(StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile))
    con.commit()
    con.close()

def viewdata():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student4")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student4 WHERE StdID=?",(id))
    con.commit()
    con.close()

def searchdata(StdID='',Firstname='',Lastname='',Dob='',Age='',Gender='',Address='',Mobile=''):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student4 WHERE StdID=? OR Firstname=? OR Lastname=? OR Dob=? "
                "OR Age=? OR Gender=? OR Address=? OR Mobile=? ",
                (StdID, Firstname, Lastname, Dob, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows



def dataupdata(id,StdID='',Firstname='',Lastname='',Dob='',Age='',Gender='',Address='',Mobile=''):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student4 SET StdID=?, Firstname=?, Lastname=? , Dob=? "
                ", Age=? , Gender=? , Address=? , Mobile=?,WHERE id=? ",(StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,id))
    con.commit()
    con.close()

studentData()