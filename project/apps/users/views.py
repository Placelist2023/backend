import json
import logging

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer

logger = logging.getLogger(__name__)


class UserDetailAPI(APIView):

    def get(self, request, *args, **kwargs):
        logger.info(request.user)
        user = CustomUser.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# this endpoint only accepts PUT requests
@api_view(['PUT'])
# the function receives the request object (url, headers, payload, etc) and the pk (user id) from the url
def update_user_info(request, pk=None):
    # find the user in the database using the id from the url
    user = CustomUser.objects.get(pk=pk)
    # deserialize the payload (convert from a json string to a python dictionary)
    payload = json.loads(request.body)
    # update the user object in the database with info from the payload
    user.first_name = payload['first_name']
    user.last_name = payload['last_name']
    user.email = payload['email']
    # save the changes
    user.save()
    # return the updated user info (serialized to json)
    return HttpResponse(json.dumps({
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }))
