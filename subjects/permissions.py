from rest_framework import permissions

class CanAddSubject(permissions.BasePermission):
    def has_permission(self, request, view):
        # Kiểm tra quyền xem danh sách học sinh
        return request.user and  request.user.username.startswith('admin')