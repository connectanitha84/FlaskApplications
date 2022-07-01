# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:40:08 2022

@author: anuaq
"""

from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysql@2022'
app.config['MYSQL_DB'] = 'UserDet'
 
mysql = MySQL(app)
 
@app.route('/')
def form():
    return render_template('index.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        passwd = request.form['password']
        fcar = request.form['fcar']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s,%s,%s)''',(fname,lname,passwd,fcar))
        mysql.connection.commit()
        cursor.close()
        return render_template('index.html',status="User registered successfully")

    
@app.route('/users')
def listusers():
        cursor = mysql.connection.cursor()
        users=cursor.execute("SELECT * from info_table")
        if users>0:
            userdetails=cursor.fetchall()
        cursor.close()
        return render_template('userdetails.html',userdetails=userdetails)
 
if __name__=='__main__':
    app.run(port=5000)