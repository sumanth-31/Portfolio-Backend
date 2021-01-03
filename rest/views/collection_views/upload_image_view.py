from django.http import JsonResponse

from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated

from rest.models import Collection, User
from rest.utils import bad_request


class UploadCollectionImage(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        user: User = request.user
        collection = request.POST.get("collection")
        image = request.FILES.get("collection_image")
        if collection is None:
            return bad_request(
                "Collection cannot be empty"
            )
        if image is None:
            return bad_request("Image is required")
        try:
            collection_obj = Collection.objects.get(id=collection, user=user)
        except:
            return bad_request("Collection not found")
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
        return JsonResponse(response_data)
