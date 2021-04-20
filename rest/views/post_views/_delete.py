import json

from django.http import JsonResponse

# Create your views here.
from rest_framework.views import Request

from rest.models import Post


def delete(self, request: Request):
    posts = Post.objects.all()
    request_data = request.data
    post_id = request_data.get("post_id")
    collection = request_data.get("collection")
    tag = request_data.get("tag")
    if post_id:
        posts = posts.filter(post_id=post_id)
    if collection:
        posts = posts.filter(collection=collection)
    if tag:
        posts = posts.filter(tag=tag)
    posts.delete()
    response_data = {"message": "Deletion successful"}
    return JsonResponse(response_data)
