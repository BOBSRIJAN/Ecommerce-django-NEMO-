from pymongo import MongoClient
from bson import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb+srv://srijan:1234@cluster0.yrnd8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['NEMO']
products_collection = db['ITEMS']

# Initial product data
initial_products = [
    {
        "_id": ObjectId(),
        "name": "Apple",
        "description": "Fresh and juicy apples from organic farms.",
        "price": 58.75,
        "image_url": "https://example.com/apple.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Banana",
        "description": "Sweet and ripe bananas packed with nutrients.",
        "price": 79.82,
        "image_url": "https://example.com/banana.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Cherry",
        "description": "Delicious red cherries, perfect for snacking.",
        "price": 89.59,
        "image_url": "https://example.com/cherry.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Date",
        "description": "Premium quality dates, rich in fiber and energy.",
        "price": 70.87,
        "image_url": "https://example.com/date.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Elderberry",
        "description": "Antioxidant-rich elderberries for a healthy boost.",
        "price": 83.2,
        "image_url": "https://example.com/elderberry.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Fig",
        "description": "Soft and sweet figs, full of natural goodness.",
        "price": 51.13,
        "image_url": "https://example.com/fig.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Grape",
        "description": "Fresh seedless grapes, great for snacks and juices.",
        "price": 65.22,
        "image_url": "https://example.com/grape.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Honeydew",
        "description": "Sweet and refreshing honeydew melons.",
        "price": 54.47,
        "image_url": "https://example.com/honeydew.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Kiwi",
        "description": "Tangy and vitamin-rich kiwis for daily health.",
        "price": 55.65,
        "image_url": "https://example.com/kiwi.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Lemon",
        "description": "Zesty and refreshing lemons for multiple uses.",
        "price": 51.09,
        "image_url": "https://example.com/lemon.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Mango",
        "description": "Sweet and juicy mangoes, a tropical delight.",
        "price": 72.50,
        "image_url": "https://example.com/mango.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Orange",
        "description": "Vitamin C-rich oranges, fresh and tangy.",
        "price": 63.25,
        "image_url": "https://example.com/orange.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Papaya",
        "description": "Ripe papayas, great for digestion and health.",
        "price": 59.45,
        "image_url": "https://example.com/papaya.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Peach",
        "description": "Soft and juicy peaches, packed with flavor.",
        "price": 77.10,
        "image_url": "https://example.com/peach.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Pear",
        "description": "Crisp and refreshing pears, rich in fiber.",
        "price": 64.30,
        "image_url": "https://example.com/pear.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Pineapple",
        "description": "Tropical pineapples with a perfect balance of sweet and tangy.",
        "price": 79.99,
        "image_url": "https://example.com/pineapple.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Plum",
        "description": "Delicious plums, packed with antioxidants.",
        "price": 55.70,
        "image_url": "https://example.com/plum.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Pomegranate",
        "description": "Nutrient-rich pomegranates full of juicy seeds.",
        "price": 88.50,
        "image_url": "https://example.com/pomegranate.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Raspberry",
        "description": "Sweet and tart raspberries, a healthy treat.",
        "price": 68.90,
        "image_url": "https://example.com/raspberry.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Strawberry",
        "description": "Fresh strawberries, perfect for desserts and smoothies.",
        "price": 79.20,
        "image_url": "https://example.com/strawberry.jpg"
    },
    {
        "_id": ObjectId(),
        "name": "Watermelon",
        "description": "Refreshing and hydrating watermelons for summer days.",
        "price": 50.50,
        "image_url": "https://example.com/watermelon.jpg"
    }
]

# Insert initial products
if products_collection.count_documents({}) == 0:
    products_collection.insert_many(initial_products)
    print("Initial products inserted successfully!")
else:
    print("Products already exist in the database.")
