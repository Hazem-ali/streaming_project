from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        isAdminCondition = super().has_permission(request, view)

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return isAdminCondition


class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(obj.review_user == request.user)
