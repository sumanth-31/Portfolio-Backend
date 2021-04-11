from django.http import JsonResponse
from django.core.paginator import Page, Paginator
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import Collection, User
from rest.utils import meta_details_generator


class GetCollections(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        user: User = request.user
        collections = Collection.objects.filter(user=user).order_by(
            "name"
        )
        query_collections = []
        for collection_obj in collections:
            curr_collection = {
                "name": collection_obj.name,
                "id": collection_obj.id
            }
            if collection_obj.image:
                image_url_raw = collection_obj.image.url
                image_url = request.build_absolute_uri(image_url_raw)
                curr_collection["image"] = image_url
            query_collections.append(curr_collection)
        response_data = {"collections": query_collections}
        return JsonResponse(response_data)
