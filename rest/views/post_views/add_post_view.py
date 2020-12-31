import json
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest.models import Post, Collection, Tag


class AddPost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_id=request.user.id
        payload = json.loads(request.body)
        collection = payload.get("collection")
        tag = payload.get("tag")
        content = payload.get("content")
        if content is None or not content:
            response_data = {"message": "Content of post cannot be empty"}
            return HttpResponseBadRequest(json.dumps(response_data), "application/json")
        if collection is None:
            collection = "article"
        if tag is None:
            tag = "general"
        collection_obj = Collection(name=collection)
        collection_obj.save()
        tag_obj = Tag(name=tag)
        tag_obj.save()
        post = Post.objects.create(user=request.user,
            content=content, collection=collection_obj, tag=tag_obj
        )
        post.save()
        response_data = {
            "post": {
                "user_id":user_id,
                "post_id": post.post_id,
                "content": post.content,
                "collection": collection,
                "tag": tag,
            },
            "message": "Added post"
        }
        return HttpResponse(json.dumps(response_data), "application/json")
