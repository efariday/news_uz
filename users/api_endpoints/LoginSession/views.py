from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from users.api_endpoints.LoginSession.serializers import LoginSessionSerializer


class LoginSessionAPIView(GenericAPIView):
    serializer_class = LoginSessionSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
