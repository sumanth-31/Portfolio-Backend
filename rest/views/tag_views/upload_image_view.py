from django.http.response import JsonResponse

from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated

from rest.models import Tag
from rest.utils import bad_request


class UploadTagImage(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        tag = request.POST.get("tag")
        image = request.FILES.get("tag_image")
        if tag is None:
            return bad_request("Tag cannot be empty")
        if image is None:
            return bad_request("Image is required")
        try:
            tag_obj = Tag.objects.get(id=tag)
        except:
            return bad_request("Tag not found")
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
        return JsonResponse(response_data)
