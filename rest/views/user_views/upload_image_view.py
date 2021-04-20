from django.http import JsonResponse

from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import User
from rest.utils import bad_request
from rest.convertors import user_to_json


class UploadProfilePic(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        image = request.FILES.get("profile_pic")
        if image is None:
            return bad_request("Image is required")
        user: User = request.user
        user.profile_pic = image
        user.save()
        response_data = {
            "user": user_to_json(request, user),
            "message": "Successfully updated profile pic",
        }
        return JsonResponse(response_data)
