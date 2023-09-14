from django.shortcuts import render
from rest_framework import generics

from apps.users.permissions import IsUnregistered
from apps.users.serializers import SignUpSerializer
from apps.users.utils import RegisterService


# Create your views here.


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsUnregistered]

    def post(self, request, *args, **kwargs):
        return RegisterService.create_user(self.serializer_class(data=request.data), request)
