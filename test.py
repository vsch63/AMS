from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from passlib.hash import sha256_crypt


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Maymonth#2021@localhost/agency_sys'
engine = db.create_engine('mysql://agent:Maymonth#2021@localhost:3307/agency_sys')
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('users', metadata, autoload=True, autoload_with=engine)

print(users.columns.keys())
query = db.select([users])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
query = db.select([users]).where(users.columns.USER_ID == 1)
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
password1 = sha256_crypt.hash('agent@2020')
query = db.insert(users).values(USER_NAME='Chakravarthi', PASSWORD=password1,USER_LEVEL=1,LAST_MOD_USER='chakravarthi')
ResultProxy = connection.execute(query)