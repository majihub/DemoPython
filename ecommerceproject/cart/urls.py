from django.urls import path, include

from . import views
app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('delete/<int:product_id>/',views.cart_delete,name='cart_delete'),
    path('full_delete/<int:product_id>/',views.full_delete,name='full_delete'),
    ]