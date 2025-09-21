from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Tout le monde peut lire
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Seuls les superusers peuvent écrire
        return request.user.is_superuser
    
    
    