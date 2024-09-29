from rest_framework import permissions


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderator").exists()

class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsOwmer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
