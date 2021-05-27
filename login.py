import os
import os.path
import shutil
import time
from shutil import copy
import pandas as pd
from flask import *
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename
import pathlib
from pathlib import Path
import sqlalchemy as db
import dbconnect  as dbc


global user_level
app = Flask(__name__)
Bootstrap(app)


@app.route('/error')
def error():
    global user_level
    # return "<p><strong>Enter correct password</strong></p>"
    return render_template("error.html",)

@app.route('/')
def login():
    global user_level
    invalidlogin = " "
    return render_template("index1.html",  invalid_login=invalidlogin, )


@app.route('/home', methods=['GET', 'POST'])
def home():
    global user_level
    messg_line=""
    return render_template("index.html",  user_level=user_level,messg_line=messg_line)


@app.route('/mainpage', methods=['GET', 'POST'])
def mainpage():
    print("Hello")
    global user_level,all_file_details,mig_dir
    username = request.form['username']
    password = request.form['password']
    metadata = db.MetaData()
    users = db.Table('users', metadata, autoload=True, autoload_with=dbc.engine)
    query = db.select([users]).where(users.columns.USER_NAME == username)
    #query = db.select([users]).where(db.and_(users.columns.USER_NAME == username , users.columns.PASSWORD == 'M'))
    ResultProxy = dbc.connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    print("**************************")
    print(ResultSet,"*************")
    testpassword = sha256_crypt.hash(password)
    print(testpassword)
    #user_level=1
    #val_password=True
    if len(ResultSet) > 0:
          user_level = ResultSet[0][3]
          val_password = sha256_crypt.verify(password, ResultSet[0][2])

    else:
         val_password = False
    
    if val_password:        
       return render_template("index.html",user_level=user_level,result="ResultSet[0][2]")
    else:
        invalid_login = "Invalid User name or Password"
        return render_template("index1.html", invalid_login=invalid_login)



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
