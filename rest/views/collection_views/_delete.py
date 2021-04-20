from django.http import JsonResponse

from rest_framework.views import Request
from rest.models import Collection, User
from rest.utils import bad_request


def delete(self, request: Request):
    user: User = request.user
    request_data = request.data
    collection_id = request_data.get("collection_id")
    if collection_id is None:
        return bad_request("collection cannot be empty")
    try:
        collection_obj: Collection = Collection.objects.get(
            id=collection_id, user=user)
        collection_obj.delete()
    except:
        return bad_request("collection not found")
    response_data = {
        "collection": collection_id,
        "message": "Collection successfully deleted",
    }
    return JsonResponse(response_data)
