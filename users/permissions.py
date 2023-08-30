from rest_framework import permissions

class CanUpdateProfile(permissions.BasePermission):
    """
    Custom permission to allow only the user or admin to update their profile.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the profile or admin
        return obj.user == request.user or request.user.is_staff

class CanViewStudentList(permissions.BasePermission):
    def has_permission(self, request, view):
        # Kiểm tra quyền xem danh sách học sinh
        return request.user and (request.user.username.startswith('gv') or request.user.username.startswith('admin'))

class CanViewStudentDetail(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kiểm tra quyền xem chi tiết thông tin học sinh
        return request.user and (request.user.username.startswith('gv') or request.user.username.startswith('admin') or obj.user == request.user)


class CanAddStudentAndTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        # Kiểm tra quyền xem danh sách học sinh
        return request.user and  request.user.username.startswith('admin')