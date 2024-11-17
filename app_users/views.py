from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from app_menu.models import UserModel
from app_users.serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _= Token.objects.get_or_create(user=user)

            return Response({
                "tokens": token.key,
                "id": user.id,
                "username": user.username,
                "phone_number": user.phone_number,
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "message": "Username or password is incorrect"
        })

class UserView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

