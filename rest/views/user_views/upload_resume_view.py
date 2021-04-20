from django.http import JsonResponse

from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.utils import bad_request
from rest.models import User
from rest.convertors import user_to_json


class UploadResume(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        resume = request.FILES.get("resume")
        if resume is None:
            return bad_request("Resume is required")
        user: User = request.user
        user.resume = resume
        user.save()
        response_data = {
            "user": user_to_json(request, user),
            "message": "Successfully updated resume",
        }
        return JsonResponse(response_data)
