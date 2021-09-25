import os
from flask import Flask, request,jsonify, render_template, url_for, json

def searchProduct(mysql): 
    cur= mysql.connection.cursor()
    query = request.args.get('q')
    try:
        cur.execute('SELECT i.id, i.name, i.brand, i.thumbnail, c.id as cityId, c.name as cityName, i.price, i.rating, s.id as sellerId, s.name as sellerName, s.logo FROM item i INNER JOIN city c ON i.city = c.id INNER JOIN seller s ON i.seller = s.id WHERE i.name LIKE %s',["%"+query+"%"])
        rv = cur.fetchall()
        json_data=[]
        contentItem = {}
        content = {}
        for result in rv:
            contentItem = {'id': result[0], 'name': result[1], 'brand': result[2],'thumbnail': result[3], 'city': {'id':result[4], 'name':result[5]}, 'price': result[6], 'rating':result[7]}
            json_data.append(contentItem)
        json_data2=[]
        content = {'query': query, 'total': len(rv), 'items': json_data, 'seller': {'id': result[8], 'name': result[9], 'logo': result[10]}}
        json_data2.append(content)
        return  jsonify(dict(json_data2))
    except:
        contentItem = {'id': 0, 'name': " ", 'brand': " ",'thumbnail': " ", 'city': {'id':0, 'name':" "}, 'price': 0.0, 'rating': 0.0}
        json_data.append(contentItem)
        content = {'query': query, 'total': 0, 'items': json_data, 'seller': {'id':0, 'name': " ", 'logo': " "}}
        dict(json_data2.append(content))
        return  jsonify(json_data2)


def searchProductDetail(id,mysql):
    cur= mysql.connection.cursor()
    try:
        cur.execute('SELECT i.id, i.name, i.brand, p.url, c.id as cityId, c.name as cityName, i.price, i.rating, i.description, s.id as sellerId, s.name as sellerName, s.logo FROM item i INNER JOIN city c ON i.city = c.id INNER JOIN seller s ON i.seller = s.id INNER JOIN picture p ON i.id = p.item WHERE i.id=%s', (id))
        rv = cur.fetchall()
        json_data=[]
        contentItem = {}
        picture = []
        for result in rv:
            picture.append(result[3])
        contentItem = {'id': result[0], 'name': result[1], 'brand': result[2],'pictures': picture, 'city': {'id':result[4], 'name':result[5]}, 'price': result[6], 'rating':result[7],'description':result[8],'seller': {'id': result[9], 'name': result[10], 'logo': result[11]}}
        json_data.append(contentItem)
        return jsonify(dict(json_data))
    except:

        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "jsonDetalle.json")
        data = json.load(open(json_url))
        return jsonify(data)



