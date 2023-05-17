from django.urls import path 
from products import views

urlpatterns = [

    path('',views.store, name="store"),
    path('cart/',views.cart, name="cart"),
    path('cheakout/',views.cheakout, name="cheakout")
]