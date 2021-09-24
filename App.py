from flask_mysqldb import MySQL
from searchProduct import searchProduct,searchProductDetail
from connection import connection,run,app


connection()

mysql = MySQL(app)

@app.route('/api/search', methods=['GET'])

def search():
    return searchProduct(mysql)

@app.route('/api/item/<id>',methods=['GET'])

def detalle(id):
    return searchProductDetail(id,mysql)

run()
    
