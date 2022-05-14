from .models import Customer, User, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from .serializers import *

SECRET_KEY = "q4t7w!z%C*F-JaNcRfUjXn2r5u8x/A?D"

class ShieldCustomerAPIView(APIView):
    def post(self, request):
        serializer = ShieldCustomerCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.data['secret_key'] != SECRET_KEY:
            return 0
        customer = Customer.objects.get(user_id=request.data['id'])

        return Response(ShieldCustomerInfoSerializer(customer).data)


class ShieldProductsAPIView(APIView):
    def post(self, request):
        if request.data['secret_key'] != SECRET_KEY:
            return 0

        products = Product.objects.all().values()
        return Response(ShieldProductListSerializer(products, many=True).data)


class ShieldUserRegistrationAPIView(APIView):
    def post(self, request):
        if request.data['secret_key'] != SECRET_KEY:
            return 0

        serializer = ShieldUserRegistration(data=request.data)
        serializer.is_valid(raise_exception=True)

        User.objects.create_user(username=request.data['username'],
                            email=request.data['email'],
                            password=request.data['password'])

        new_user = User.objects.get(email=request.data['email'])
        Customer.objects.create(user=new_user, name=request.data['name'], email=request.data['email'])

        return Response({'post': 'new user was created'})


class ShieldUserLoginAPIView(APIView):
    def post(self, request):
        serializer = ShieldUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.data['secret_key'] != SECRET_KEY:
            return 0

        user = User.objects.get(username=request.data['username'])

        if check_password(request.data['password'], user.password):
            return Response(user.id)
        else:
            return Response("WRONG PASSWORD")


