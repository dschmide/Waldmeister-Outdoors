#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from WaldmeisterMap.models import UserArea

#from WaldmeisterMap.models import RegisteredUser


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserArea
        fields = ('label', 'public', 'polygon', 'creator')

# class RegisteredUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = RegisteredUser
#         fields = ('username', 'password', 'displayname')

#     def create(self, validated_attrs):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_attrs)