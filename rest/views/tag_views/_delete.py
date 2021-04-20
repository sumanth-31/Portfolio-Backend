from django.http import JsonResponse

# Create your views here.
from rest_framework.views import Request

from rest.models import Tag
from rest.utils import bad_request


def delete(self, request: Request):
    request_data = request.data
    tag_id = request_data.get("tag_id")
    if tag_id is None:
        return bad_request("tag cannot be empty")
    try:
        tag_obj = Tag.objects.get(tag_id=tag_id)
    except:
        return bad_request("tag not found")
    tag_obj.delete()
    response_data = {
        "tag": tag_id,
        "message": "Tag successfully deleted",
    }
    return JsonResponse(response_data)
