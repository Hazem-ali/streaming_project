from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response

from rest_framework.authtoken.models import Token


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

            token, is_created = Token.objects.get_or_create(user=account)
            data['token'] = token.key

            return Response(data)
        return Response(serializer.errors)
