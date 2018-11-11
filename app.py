from flask import Flask, render_template, request
import sqlite3

#cur.execute needed first to establish the table

sql = '''CREATE TABLE IF NOT EXISTS Directory (id INTEGER PRIMARY KEY, OwnerLast TEXT, OwnerFirst TEXT, PetName TEXT, PetType TEXT, NextAppt DATE, Notes TEXT)'''

def AddRecord():
    db = sqlite3.connect("./directory.db")
    cur = db.cursor()
    newRecord = '''INSERT INTO directory (OwnerLast, OwnerFirst, PetName, PetType)VALUES('Trout','Valeri','Samantha', 'Cat')'''
    cur.execute(newRecord)
    db.commit()
    results = cur.fetchall()
    db.close()
    return results


def sendSQL(sql):
    db = sqlite3.connect("./directory.db")
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    results = cur.fetchall()
    db.close()
    return results
    print(results)
def getData():
    db = sqlite3.connect("./directory.db")
    cur = db.cursor()
    sql = '''SELECT * FROM directory'''
    cur.execute(sql)
    db.commit()
    results = cur.fetchall()
    db.close()
    return results


app = Flask(__name__)

# @ = decorator to establish page.  Expects a function defined next
@app.route('/')
def index():
    return "Welcome to Dr. Val's Vetenary Hosptial"
#
#
@app.route('/directory', methods=['GET','POST','NEW'])
def manageDirectory():
    directory = getData()
    if request.method == "GET":
        sql = '''SELECT * FROM directory WHERE PetName ="Samantha" '''
        sendSQL(sql)

    elif request.method == "NEW":
        AddRecord()
    elif request.method=="POST":
        sql ='''INSERT INTO directory (note) VALUES ("{}")'''.format(request.form["Notes"])
        sendSQL(sql)
    directory = getData()
    return render_template("directory.html", PetName="PetName")


app.run()

# make change for GIT