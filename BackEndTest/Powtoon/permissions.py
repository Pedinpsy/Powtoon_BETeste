from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not (request.method in permissions.SAFE_METHODS):
            return obj.owner == request.user
        return True

class CanShare(permissions.BasePermission):
    def has_permission(self, request, view):
       return "share.share_powtoon" in request.user.get_user_permissions()
      
