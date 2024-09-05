from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users edit their own profile
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """
    Allow users to update their own status
    """
    def has_object_permission(self, request, view, obj):
        """
        Check the user is trying to updtade their own status
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user.id == request.user.id