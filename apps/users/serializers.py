from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.users.models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return validate_password(value)

    def validate_email(self, value):
        queryset = CustomUser.objects.all()
        return validate_email(value, queryset)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}
