from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'hido' #it is a secret that should be secured
api = Api(app)

#for security needed
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
jwt = JWT(app, authenticate, identity) #JWT creates a new route /AUTH which authenticates the user




api.add_resource(Item, '/item/<string:name>') #hhtp://127.0.0.1:5000/student/<name>
api.add_resource(ItemList, '/items') #hhtp://127.0.0.1:5000/student/<name>
api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
    app.run(port = 5000, debug = True)