from flask_mysqldb import MySQL
from Services.searchProduct import searchProduct,searchProductDetail
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'nnsgluut5mye50or.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'lgab4tkno4x6egda'
app.config['MYSQL_PASSWORD'] = 'owxq5zm80co70gcm'
app.config['MYSQL_DB'] = 'zx7ecatofxxbvaz3'
    
# settings
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/api/search', methods=['GET'])

def search():
    return searchProduct(mysql)

@app.route('/api/item/<id>',methods=['GET'])

def detalle(id):
    return searchProductDetail(id,mysql)

if __name__ == '__main__':   
    app.run(port = 8008, debug = True)

    
