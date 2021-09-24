from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

def connection(): 
    print("aca fue")
    app.config['MYSQL_HOST'] = 'nnsgluut5mye50or.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    app.config['MYSQL_USER'] = 'lgab4tkno4x6egda'
    app.config['MYSQL_PASSWORD'] = 'owxq5zm80co70gcm'
    app.config['MYSQL_DB'] = 'zx7ecatofxxbvaz3'
    
    # settings
    app.secret_key = 'mysecretkey'

def run():
    print("aca tambien")
    app.run(port = 8008, debug = True)
        
