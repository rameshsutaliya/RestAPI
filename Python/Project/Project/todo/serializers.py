from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Project.todo.models import TodoList, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# Todo app api


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ['title', 'discription', 'created', 'due_date']
