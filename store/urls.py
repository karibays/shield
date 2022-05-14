from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.store, name='store'),

    path('api/customer', api.ShieldCustomerAPIView.as_view(), name='apiCustomer'),
    path('api/productList', api.ShieldProductsAPIView.as_view(), name='apiProductList'),
    path('api/register', api.ShieldUserRegistrationAPIView.as_view(), name='apiUserRegistration'),
    path('api/login', api.ShieldUserLoginAPIView.as_view(), name='apiUserLogin'),

    path('product/<int:pk>/', views.productdetail, name='productdetail'),
    path('product_category/<str:pk>/', views.productCategory, name='productCategory'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]
