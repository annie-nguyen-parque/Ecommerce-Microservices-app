from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
# 'mysql://<user>:<password>@<service>/<table>'
CORS(app)

db = SQLAlchemy(app)

@dataclass # object Product will be serializable
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False) # no increment
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass # object Product will be serializable
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True) # increment
    user_id = db.Column(db.Integer)
    Product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')
    # this pair has to be unique

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    return jsonify(req.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


