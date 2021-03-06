from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(name=validated_data.get('name'), email=validated_data.get('email'), )
        user.set_password(raw_password=validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'image', 'created_at', 'updated_at']
