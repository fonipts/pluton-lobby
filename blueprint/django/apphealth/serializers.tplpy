from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'linenos']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
