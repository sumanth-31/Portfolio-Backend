from django.http import JsonResponse
from django.core.paginator import Page, Paginator
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import Collection, User


class GetCollections(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        user: User = request.user
        page = 1
        per_page = 10
        request_data = request.GET
        if request_data.get("page"):
            page = request_data["page"]
        if request_data.get("per_page"):
            per_page = request_data["per_page"]
        collections = Collection.objects.filter(user=user).order_by(
            "name"
        )  # collection is collection obj to cascade delete
        paginator: Paginator = Paginator(collections, per_page)
        page_obj: Page = paginator.get_page(page)
        query_collections = []
        for collection_obj in page_obj.object_list:
            curr_collection = {
                "name": collection_obj.name,
                "id": collection_obj.id
            }
            if collection_obj.image:
                image_url_raw = collection_obj.image.url
                image_url = request.build_absolute_uri(image_url_raw)
                curr_collection["image"] = image_url
            query_collections.append(curr_collection)
        meta = {
            "currPage": page_obj.number,
            "pages_count": paginator.num_pages,
            "items_count": paginator.count,
        }
        response_data = {"collections": query_collections, "meta": meta}
        return JsonResponse(response_data)
