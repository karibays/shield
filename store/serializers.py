from rest_framework import serializers


class ShieldProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    digital = serializers.BooleanField(default=False)
    image = serializers.CharField(max_length=200)


class ShieldUserRegistration(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    secret_key = serializers.CharField()


class ShieldCustomerInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

class ShieldCustomerCheckSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    secret_key = serializers.CharField()

class ShieldUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)




