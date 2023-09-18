from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from apps.users.tokens import create_jwt_pair_for_user


def send_email_confirmation(email):
    pass


class RegisterService:
    @staticmethod
    def create_user(serializer, request):
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_email_confirmation(user.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def login_user(serializer):
    user = authenticate(
        email=serializer.validated_data["email"],
        password=serializer.validated_data["password"]
    )

    if user is not None:
        tokens = create_jwt_pair_for_user(user)
        response = {"message": "Login Successful", "tokens": tokens}
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        return Response(
            data={"message": "Invalid email or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
