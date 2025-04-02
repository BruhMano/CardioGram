from rest_framework.permissions import BasePermission, SAFE_METHODS
from sympy import false


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff

class IsAdminOrIsOwnerReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.method in SAFE_METHODS:
            try:
                return obj.user == request.user
            except AttributeError:
                return obj == request.user

