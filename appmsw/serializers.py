# serializers.py
from rest_framework import serializers
from appmsw.models import Param, Comment, SysOption
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'creation_date', 'author', 'param']
        read_only_fields = ['creation_date', 'author']

class ParamSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Param
        fields = [
            'id', 'name', 'category', 'desc', 'option',
            'json', 'creation_date', 'user', 'public', 'enabled', 'comments'
        ]
        read_only_fields = ['creation_date', 'user']

class SysOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOption
        fields = [
            'id', 'name', 'category', 'desc', 'option',
            'json', 'creation_date', 'public', 'enabled'
        ]
        read_only_fields = ['creation_date']