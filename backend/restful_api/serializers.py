from rest_framework import serializers
from restful_api.models import UserArea
from restful_api.models import Vegetation

from django.contrib.auth import get_user_model
User = get_user_model()


class AreaSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),  # Or User.objects.filter(active=True)
        required=False,
        allow_null=True,
        default=None,
    )

    # Get the current user from request context
    def validate_creator(self, value):
        return self.context['request'].user

    class Meta:
        model = UserArea
        fields = ('label', 'public', 'polygon', 'creator', 'id')


class VegetationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetation
        fields = ('ek72', 'geom')
