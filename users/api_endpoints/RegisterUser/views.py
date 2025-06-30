from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from users.api_endpoints.RegisterUser.serializers import RegisterInputSerializer


class RegisterUserAPIView(GenericAPIView):
    serializer_class = RegisterInputSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"detail": "User created successfully"}, status=status.HTTP_201_CREATED)
