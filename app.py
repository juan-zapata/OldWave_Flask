
from flask_mysqldb import MySQL
from Services.searchProduct import searchProduct,searchProductDetail
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-1.cztqwnr3tkxs.us-west-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'root1234'
app.config['MYSQL_DB'] = 'flaskdb'
    
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
    app.run(port = 8080, debug = True)
