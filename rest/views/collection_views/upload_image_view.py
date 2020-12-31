import json
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest.models import Collection


class UploadCollectionImage(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        collection = request.POST["collection"]
        image = request.FILES.get("collection_image")
        if collection is None:
            return HttpResponseBadRequest(
                "Collection cannot be empty", "application/json"
            )
        if image is None:
            return HttpResponseBadRequest("Image is required", "application/json")
        try:
            collection_obj = Collection.objects.get(name=collection)
        except:
            return HttpResponseBadRequest("Collection not found", "application/json")
        print(image)
        collection_obj.image = image
        collection_obj.save()
        response_data = {
            "collection": {
                "name": collection_obj.name,
                "image": request.build_absolute_uri(collection_obj.image.url),
            },
            "message": "Successfully uploaded image for tag",
        }
        return HttpResponse(json.dumps(response_data), "application/json")
