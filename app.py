from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Product

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la app
@app.route('/')
def home():
    product = db['products']
    productReceived = product.find()
    return render_template('index.html', product = productReceived)

#method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantify = request.form['quantify']

    if name and price and quantify:
        product = Product(name, price, quantify)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantify' : quantify
        })
        return redirect(url_for('home'))
    else:
        return notFound()
    
#method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

#method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantify = request.form['quantify']

    if name and price and quantify:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantify' : quantify}})
        response = jsonify({'message' : 'Producto ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()
    
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message' : 'No he encontrado ' + request.url,
        'status' : '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)