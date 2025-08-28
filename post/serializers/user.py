from rest_framework import serializers
from post.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'role', 'is_active', 'is_staff', 'otp_code', 'otp_created_at']
        read_only_fields = ['is_active', 'is_staff', 'otp_code', 'otp_created_at']
        extra_kwargs = {'password': {'write_only': True}}