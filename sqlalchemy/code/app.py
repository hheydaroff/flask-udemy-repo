from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from datetime import timedelta
from db import db

app = Flask(__name__)
app.secret_key = 'hido' #it is a secret that should be secured
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # We turn off the modification tracking from flask.sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'

@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)



#for security needed
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
jwt = JWT(app, authenticate, identity) #JWT creates a new route /AUTH which authenticates the user




api.add_resource(Item, '/item/<string:name>') #hhtp://127.0.0.1:5000/student/<name>
api.add_resource(ItemList, '/items') #hhtp://127.0.0.1:5000/student/<name>
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')



if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 5000, debug = True)