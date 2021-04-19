from django.http import JsonResponse

from rest_framework.views import Request
from rest.models import Collection, User
from rest.utils import bad_request


def delete(self, request: Request):
    user: User = request.user
    collection = request.GET.get("collection")
    if collection is None:
        return bad_request("collection cannot be empty")
    try:
        collection_obj: Collection = Collection.objects.get(
            id=collection, user=user)
        collection_obj.delete()
    except:
        return bad_request("collection not found")
    response_data = {
        "collection": collection,
        "message": "Collection successfully deleted",
    }
    return JsonResponse(response_data)
