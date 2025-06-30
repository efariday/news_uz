from rest_framework import serializers
from django.utils import timezone
from users.models import User


class ConfirmTokenSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, value):
        try:
            user = User.objects.get(activation_token=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid token")

        if user.is_active:
            raise serializers.ValidationError("User already activated")

        expiry_time = user.created_at + timezone.timedelta(seconds=3600)
        if timezone.now() > expiry_time:
            raise serializers.ValidationError("Token expired")

        return value

    def save(self, **kwargs):
        token = self.validated_data["token"]
        user = User.objects.get(activation_token=token)
        user.is_active = True
        user.activation_token = None
        user.save()
        return user
