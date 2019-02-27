from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from blockchain import RPCClient

from .models import *
from .serializers import UserSerializer


class CreateUser(APIView):
    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if RPCClient().create_user(serializer.validated_data):
                serializer.save()
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoID(APIView):
    @staticmethod
    def get(_, user_id):
        if user_id == settings.ANONYMOUS_ID:
            return Response({
                'user_id': user_id,
                'nickname': 'Anonymous',
                'email': 'anonymous@infnote.com',
                'avatar': None,
                'bio': '',
                'signature': None,
                'topics': 0,
                'replies': 0,
                'date_created': 0,
                'block_height': 0,
                'block_time': 0,
            })
        user = User.objects.get(user_id=user_id)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)
