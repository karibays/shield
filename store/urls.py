from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/<int:pk>/', views.productdetail, name='productdetail'),
    path('product_category/<str:pk>/', views.productCategory, name='productCategory'),

    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]
