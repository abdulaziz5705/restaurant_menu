from unittest.mock import patch

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app_menu.models import UserModel


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    phone_number = serializers.CharField(max_length=20,write_only=True, validators=[UniqueValidator(queryset=UserModel.objects.all())])
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'phone_number']


    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords must match')
        return attrs

    def validate_phone_number(self, phone_number: str):
        phone_number = phone_number.strip()
        if not phone_number.startswith('+998'):
            raise serializers.ValidationError('Phone number must start with +998')

        if not phone_number[4:].isdigit():
            raise serializers.ValidationError('Phone number have been only numbers')
        return phone_number
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = UserModel(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=20)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
