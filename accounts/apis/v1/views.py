from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(["GET"])
def profile(requests):
    """
    Show user profile
    """
    serializer = UserSerializer(requests.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
    