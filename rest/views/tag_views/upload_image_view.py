import json
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest.models import Tag


class UploadTagImage(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        collection = request.POST["tag"]
        image = request.FILES.get("tag_image")
        if collection is None:
            return HttpResponseBadRequest("Tag cannot be empty", "application/json")
        if image is None:
            return HttpResponseBadRequest("Image is required", "application/json")
        try:
            tag_obj = Tag.objects.get(name=collection)
        except:
            return HttpResponseBadRequest("Collection not found", "application/json")
        print(image)
        tag_obj.image = image
        tag_obj.save()
        response_data = {
            "tag": {
                "name": tag_obj.name,
                "image": request.build_absolute_uri(tag_obj.image.url),
            },
            "message": "Successfully uploaded image for tag",
        }
        return HttpResponse(json.dumps(response_data), "application/json")
