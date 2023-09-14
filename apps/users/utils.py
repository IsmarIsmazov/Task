from rest_framework import status
from rest_framework.response import Response


def send_email_confirmation(email):
    pass


class RegisterService:
    @staticmethod
    def create_user(serializer, request):
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_email_confirmation(user.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
