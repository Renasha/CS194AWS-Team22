from rest_framework import permissions

#Write to Consumer but read to everyone 
class IsConsumer(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
    # Read-only permissions are allowed for any request 
        if request.method in permissions.SAFE_METHODS:
            return True
    # Write permissions are only allowed to the author of a post
        return obj.consumer == request.user

#Only consumer can read and write 
class IsConsumerStrict(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.consumer == request.user