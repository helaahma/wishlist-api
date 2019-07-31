from rest_framework.permissions import BasePermission
from datetime import date


class IsWhat(BasePermission):
	message = "You must be a staff or the owner of this item"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False
