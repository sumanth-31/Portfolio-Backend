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
        request_data = request.GET
        search_query = request_data.get("search_query")
        collections = Collection.objects.filter(user=user).order_by(
            "name"
        )
        if search_query:
            collections = collections.filter(name__icontains=search_query)
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
