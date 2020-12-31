import json
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest.models import Tag, Post


class DeleteTag(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tag = request.GET.get("tag")
        collection = request.GET.get("collection")
        if tag is None:
            response_data = {"message": "tag cannot be empty"}
            return HttpResponseBadRequest(json.dumps(response_data), "application/json")
        try:
            if collection is None:
                tag_obj = Tag.objects.get(name=tag)
            else:
                tag_obj = Post.objects.filter(tag=tag, collection=collection)
        except:
            response_data = {"message": "tag or collection not found"}
            return HttpResponseBadRequest(json.dumps(response_data), "application/json")
        tag_obj.delete()
        response_data = {
            "tag": tag,
            "collection": collection,
            "message": "Tag successfully deleted",
        }
        return HttpResponse(json.dumps(response_data), "application/json")
