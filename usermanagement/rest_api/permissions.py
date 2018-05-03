from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'PUT' 'OPTIONS']

class IsPutOrIsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        # allow all PUT requests
        if request.method in ['PUT', 'GET'] and (request.user.is_authenticated or request.user.is_superuser):
            print('in if')
            return True

        # Otherwise, only allow authenticated requests
        # Post Django 1.10, 'is_authenticated' is a read-only attribute
        return request.user and request.user.is_superuser