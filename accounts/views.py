from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
#  Import serializers used for registering and showing user profile data
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response #  Used to return HTTP responses with data and status codes
from rest_framework import status  #for status code

User = get_user_model()


class RegisterView(APIView):

    #for register  new user
    def post(self, request):  # Handles POST requests to /register/
        serializer = RegisterSerializer(data=request.data)   # Bind incoming JSON data to the RegisterSerializer

        if serializer.is_valid():
        # Check if the data is valid (email, password, etc.)
            serializer.save()
            return Response({"message": "user registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  View for Accessing & Updating Profile  #


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Only allow access to users who are authenticated (using JWT token)

    def get(self, request):     # Handle GET request to /profile/ → return current user info

        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

        # Handle PUT request to /profile/ → update user info (like first_name, last_name)
    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
