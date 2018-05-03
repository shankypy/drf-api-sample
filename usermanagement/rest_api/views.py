from django.shortcuts import render
from rest_api.models import Task
from rest_framework import generics, permissions, renderers, viewsets
from rest_api.serializers import EmployeeTaskSerializer, AdminTaskSerializer, UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from rest_api import permissions
from django.db.models import Q

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsPutOrIsAdmin,)
    queryset = Task.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        else:
            tasks = []
            tasks.append(Task.objects.filter(user=self.request.user))
            tasks.append(Task.objects.filter(group__name=self.request.user.groups))
            print('user group', self.request.user.groups)
            user_gorup = Group.objects.filter(user=self.request.user)
            user = User.objects.filter(groups__name='employee')
            return Task.objects.filter(Q(group=user_gorup) | Q(user=self.request.user))

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminTaskSerializer
        return EmployeeTaskSerializer
