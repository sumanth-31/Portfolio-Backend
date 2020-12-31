import json
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UploadResume(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        resume = request.FILES.get("resume")
        if resume is None:
            return HttpResponseBadRequest("Resume is required", "application/json")
        user = request.user
        user.resume = resume
        user.save()
        response_data = {
            "user": {
                "name": user.name,
                "email": user.email,
                "resume": request.build_absolute_uri(user.resume.url),
            },
            "message": "Successfully updated resume",
        }
        return HttpResponse(json.dumps(response_data), "application/json")
