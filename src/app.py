from flask import Flask, jsonify, request

products = [
    {
        "id": 1,
        "name": "product1"
    },
    {
        "id": 2,
        "name": "product2"
    }
]

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello to my dockerized Flask app'


@app.route('/products')
def get_products():
    return jsonify(products)


@app.route('/products/<int:id>')
def get_product(id):
    for product in products:
        if product['id'] == id:
            return jsonify(product)
    return "product with it {} is not found".format(id), 404


@app.route('/products', methods=['POST'])
def post_product():
    request_product = request.json

    # generate new id
    new_id = max([product['id'] for product in products]) + 1

    new_product = {
        'id': new_id,
        'name': request_product['name']
    }

    products.append(new_product)

    return jsonify(new_product), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
