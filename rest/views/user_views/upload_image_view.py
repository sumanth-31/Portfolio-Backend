import json
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UploadProfilePic(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        image = request.FILES.get("profile_pic")
        if image is None:
            return HttpResponseBadRequest("Image is required", "application/json")
        user = request.user
        user.image = image
        user.save()
        response_data = {
            "user": {
                "name": user.name,
                "email": user.email,
                "image": request.build_absolute_uri(user.image.url),
            },
            "message": "Successfully updated profile pic",
        }
        return HttpResponse(json.dumps(response_data), "application/json")
