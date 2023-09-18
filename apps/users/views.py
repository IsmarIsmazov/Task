from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.permissions import IsUnregistered
from apps.users.serializers import SignUpSerializer, LoginSerializer
from apps.users.utils import RegisterService, login_user


# Create your views here.


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsUnregistered]

    def post(self, request, *args, **kwargs):
        return RegisterService.create_user(self.serializer_class(data=request.data), request)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [IsUnregistered]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return login_user(serializer)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
