from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework import status

# from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logout Success'})


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()

            data = {}
            data['response'] = 'Success'
            data['username'] = account.username
            data['email'] = account.email

            # Token Authentication
            token, is_created = Token.objects.get_or_create(user=account)
            data['token'] = token.key

            # JWT Authentication
            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            # }

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
