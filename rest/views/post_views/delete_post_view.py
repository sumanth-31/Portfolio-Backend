from django.http import JsonResponse

# Create your views here.
from rest_framework.views import APIView,Request
from rest_framework.permissions import IsAuthenticated

from rest.models import Post

class DeletePost(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request:Request):
        posts=Post.objects.all()
        post_id = request.GET.get("post_id")
        collection=request.GET.get("collection")
        tag=request.GET.get("tag")
        if post_id is None:
            posts=posts.filter(id=post_id)
        if collection is not None:
            posts=posts.filter(collection=collection)
        if tag is not None:
            posts=posts.filter(tag=tag)
        posts.delete()
        response_data = {"message": "Deletion successful"}
        return JsonResponse(response_data)
