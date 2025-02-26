from django import template
from pymongo import MongoClient
from bson import ObjectId

register = template.Library()

client = MongoClient('mongodb+srv://srijan:1234@cluster0.yrnd8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['NEMO']
products_collection = db['ITEMS']

@register.filter
def get_product(products, product_id):
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        product['id'] = str(product['_id'])
    return product
