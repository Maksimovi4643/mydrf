from rest_framework import serializers
from .models import Skaters


class SkatersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Skaters
        fields = "__all__"
