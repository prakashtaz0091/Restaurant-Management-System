from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer

@api_view(["GET"])
def profile(request):
    
    serializer = UserProfileSerializer(request.user)
    
    return Response(serializer.data)


