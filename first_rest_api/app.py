from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


# POST - used to receive data as a server
# GET - used to send data back only as a server

# Let's create a store

STORES= [
    { 
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST /store data: {name:} -> Create  a new store given the name
# GET /store/<string:name> 
# GET /store
# POST /store/<string:name>/item {name:, price:}
# GET /store/<string:name>/item

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    STORES.append(new_store)
    return jsonify(new_store)



@app.route('/store/<string:name>', methods = ['GET'])
def get_store(name):
    for store in STORES:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})



@app.route('/store', methods = ['GET'])
def get_stores():
    return jsonify({'stores': STORES})



@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    request_items = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found.'})



@app.route('/store/<string:name>/item', methods = ['GET'])
def get_items_in_store(name):
    for store in STORES:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})



app.run(port = 5050)