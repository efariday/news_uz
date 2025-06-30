from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

from users.api_endpoints.LogoutSession.serializers import LogoutSessionSerializer


class LogoutSessionAPIView(GenericAPIView):
    serializer_class = LogoutSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
