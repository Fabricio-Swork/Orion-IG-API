from rest_framework.permissions import BasePermission

class RequireGroup(BasePermission):
    required_group = None

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name=self.required_group).exists()