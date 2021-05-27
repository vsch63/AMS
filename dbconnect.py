import configparser
import sqlalchemy as db
from sys import platform

config = configparser.RawConfigParser()


if (platform == 'win32'):
    os = 'Windows'
else:
    os = 'Linux'

file_with_path = 'resource/ams.properties'
config.read(file_with_path)
details_dict = dict(config.items(os))
server = details_dict['server']
database = details_dict['database']
db_type=details_dict['db_type']
user = details_dict['user']
port = details_dict['port']
password = details_dict['password']
credentials=db_type+'://'+str(user)+":" + str(password) + "@" + str(server) + ":" + port + "/" + database
engine = db.create_engine(credentials)
connection = engine.connect()
metadata = db.MetaData()

