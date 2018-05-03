from django.contrib.auth.models import User, Group
from rest_api.models import Task
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework.validators import UniqueValidator


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name', 'permissions']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'is_staff', 'is_superuser', 'groups']

    def create(self, validated_data):
        try:
            user = User(
                username=validated_data['username'],
                is_staff=validated_data['is_staff'],
                is_superuser=validated_data['is_superuser'],
            )
            user.set_password(validated_data['password'])
            user.save()
            group = Group.objects.get(name__in=validated_data['groups'])
            group.user_set.add(user)
            return user
        except Exception as e:
            print('error', e)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('email', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.set_password(validated_data['password'])
        instance.groups = validated_data.get('groups', instance.groups)
        instance.save()
        return instance


class AdminTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'id', 'task_name', 'task_progress', 'user', 'group']


class EmployeeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'id', 'task_name', 'task_progress', 'user', 'group']
        read_only_fields = ('user', 'task_name', 'group')
