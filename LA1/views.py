from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required
import json
from bson import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb+srv://srijan:1234@cluster0.yrnd8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['NEMO']
products_collection = db['ITEMS']
orders_collection = db['USER_ORDERS']

def Home(request):
    products = list(products_collection.find({}))
    if request.user.is_authenticated:
        user_name = request.user.first_name
        return render(request, 'LA1/home.html', {'products': products, 'user_name': user_name, 'request': request})
    return render(request, 'LA1/home.html', {'products': products, 'request': request})

@login_required(login_url='/accounts/login/')
def Products(request):
    user_name = request.user.first_name
    products = list(products_collection.find({}))
    for product in products:
        product['id'] = str(product['_id'])

    return render(request, 'LA1/Products.html', {'user_name': user_name, 'products': products})

# 🛒 Add product to cart
def add_to_cart(request, product_id):
    if request.method == 'POST':
        try:
            if not ObjectId.is_valid(product_id):
                return JsonResponse({'status': 'error', 'message': 'Invalid product ID'}, status=400)

            product = products_collection.find_one({'_id': ObjectId(product_id)})
            if not product:
                return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)

            # 🛒 Store cart in session (convert ObjectId to string)
            cart = request.session.get('cart', {})
            quantity = int(json.loads(request.body).get('quantity', 1))
            cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
            request.session['cart'] = cart
            request.session.modified = True  # Ensure session updates
            return JsonResponse({'status': 'success', 'cart': cart})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error'}, status=400)

# 🛒 View and manage the shopping cart
def cart_view(request):
    """View and manage the shopping cart."""
    name = request.user.first_name
    cart = request.session.get('cart', {})
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product_id = data.get("product_id")

            if product_id and product_id in cart:
                del cart[product_id]  # Remove item
                request.session["cart"] = cart
                return JsonResponse({"status": "success"})
            return JsonResponse({"status": "error", "message": "Item not found in cart"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    products = {}
    for product_id in cart.keys():
        product = products_collection.find_one({"_id": ObjectId(product_id)})
        if product:
            products[product_id] = {
                "name": product.get("name", "Unknown"),
                
                "price": product.get("price", 0)
            }
    return render(request, 'LA1/cart.html', {'cart': cart, 'products': products})

# ✅ Checkout and store order in MongoDB
@login_required(login_url='/accounts/login/')
def checkout(request):
    if request.method == 'POST':
        user_id = request.user.id  # Get logged-in user ID
        user_email = request.user.email  # Get logged-in user email
        cart = request.session.get('cart', {})  # Retrieve cart from session

        if not cart:
            return render(request, 'LA1/cart.html', {'error': 'Cart is empty!'})  # Prevent checkout if cart is empty

        # Create order data
        order = {'user_id': user_id, 'items': cart, 'status': 'pending','user_email': user_email}
        order_id = orders_collection.insert_one(order).inserted_id  # Save order to MongoDB

        # Clear the cart after checkout
        request.session['cart'] = {}
        request.session.modified = True
        return render(request, 'LA1/checkout_success.html', {'order_id': order_id,'user_email': user_email})  # Show success page
    return redirect('cart_view')  # Redirect to cart if method is not POST

def logout_view(request):
    auth_logout(request)
    return redirect('/')
