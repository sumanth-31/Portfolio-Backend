import json
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest.models import Post, Collection


class DeleteCollection(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        collection = request.GET.get("collection")
        tag = request.GET.get("tag")
        if collection is None:
            response_data = {"message": "collection cannot be empty"}
            return HttpResponseBadRequest(json.dumps(response_data), "application/json")
        try:
            if tag is None:
                posts = Collection.objects.get(name=collection)
            else:
                posts = Post.objects.filter(collection=collection, tag=tag)

        except:
            response_data = {"message": "collection or tag not found"}
            return HttpResponseBadRequest(json.dumps(response_data), "application/json")
        posts.delete()
        response_data = {
            "collection": collection,
            "tag": tag,
            "message": "Collection in tag successfully deleted",
        }
        return HttpResponse(json.dumps(response_data), "application/json")
