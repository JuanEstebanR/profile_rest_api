from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile
from profiles_api.serializers import HelloSerializer, UserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile

# Create your views here.


class HelloApiView(APIView):
    """
    Test API View
    """
    serializers_class = HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'messages': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """
        Create a hello message with our name
        :param request:
        :return:
        """
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} this is an post api view'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Update an object
        :param request:
        :return:
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """

        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """

        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API view"""
    serializer_class = HelloSerializer

    def list(self, request):
        """
        Return a hello message
        :param request:
        :return:
        """
        api_viewSet = [
            'Use actions like (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello form a ViewSet', 'api_viewSet': api_viewSet})

    def create(self, request):
        """Create a new helo message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello from a view set {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Handle getting an object by its ID
        :param request:
        :param pk:
        :return:
        """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """
        Handle updating and object
        :param request:
        :param pk:
        :return:
        """
        return Response({'http_method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        """
        Handle updating part of an object
        :param request:
        :param pk:
        :return:
        """
        return Response({'http_method': 'PATH'})

    def destroy(self, request, pk=None):
        """
        Handle removing an object
        :param request:
        :param pk:
        :return:
        """
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
