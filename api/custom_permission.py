from rest_framework.permissions import BasePermission

class IsConsultaUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Consultores').exists()