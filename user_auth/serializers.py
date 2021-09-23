from django.contrib.auth.models import User
from rest_framework import serializers

from user_auth.models import UserInput


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['id', 'input', 'datetime', 'user']


class Payload(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['input', 'datetime']


class UserSerializer(serializers.ModelSerializer):
    payload = Payload(source='userinput_set', many=True, read_only=True)
    user_id = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['status', 'user_id', 'username', 'payload']

    def get_user_id(self, obj):
        return obj.pk

    def get_status(self, obj):
        return obj.is_active
