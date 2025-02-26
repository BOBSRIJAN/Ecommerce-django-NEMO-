from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('logout/', views.logout_view, name="logout"),
    path('Products/', views.Products, name="Products"),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name="checkout"),
]
