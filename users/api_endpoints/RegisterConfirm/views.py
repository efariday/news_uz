from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from users.api_endpoints.RegisterConfirm.serializers import ConfirmTokenSerializer


class RegisterConfirmAPIView(GenericAPIView):
    serializer_class = ConfirmTokenSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Account activated"}, status=status.HTTP_200_OK)
