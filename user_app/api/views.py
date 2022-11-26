from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response



class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data)
