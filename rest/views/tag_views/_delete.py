from django.http import JsonResponse

# Create your views here.
from rest_framework.views import Request

from rest.models import Tag
from rest.utils import bad_request


def delete(self, request: Request):
    tag = request.GET.get("tag")
    if tag is None:
        return bad_request("tag cannot be empty")
    try:
        tag_obj = Tag.objects.get(name=tag)
    except:
        return bad_request("tag not found")
    tag_obj.delete()
    response_data = {
        "tag": tag,
        "message": "Tag successfully deleted",
    }
    return JsonResponse(response_data)
