from rest_framework import serializers
from users.models import User
import uuid
from django.core.mail import send_mail


class RegisterInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        activation_token = str(uuid.uuid4())

        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            is_active=False,
            activation_token=activation_token
        )

        send_mail(
            subject="Activate your account",
            message=f"Your activation token: {activation_token}",
            from_email="noreply@news.uz",
            recipient_list=[user.email],
            fail_silently=False,
        )

        return user
