import json
from django.http import JsonResponse
from rest_framework.views import Request
from rest.models import Post, Collection, Tag
from rest.utils import bad_request, object_to_dictionary
from rest.constants import PRIVACY_CLASSES
from rest.convertors import post_to_json


def put(self, request: Request):
    user = request.user
    request_data = request.data
    post_id = request_data.get("post_id")
    if not post_id:
        return bad_request("post_id cannot be empty")
    post_list = Post.objects.all().filter(user=user, post_id=post_id)
    if not post_list:
        return bad_request("No Such Post Exists!")
    post: Post = post_list[0]
    new_title = request_data.get("title", None)
    new_content = request_data.get("content", None)
    new_privacy = request_data.get("privacy", None)
    new_collection = request_data.get("collection", None)
    new_tag = request_data.get("tag", None)
    if new_privacy and new_privacy not in PRIVACY_CLASSES:
        return bad_request("Invalid Privacy Value!")
    if new_title:
        post.title = new_title
    if new_content:
        post.content = new_content
    if new_privacy:
        post.privacy = new_privacy
    if new_collection:
        collection_obj = Collection.objects.get_or_create(
            name=new_collection, user=user)[0]
        post.collection = collection_obj
    if new_tag:
        tag_obj = Tag.objects.get_or_create(name=new_tag, user=user)[0]
        post.tag = tag_obj
    post.save()
    response_data = {
        "post": post_to_json(post),
        "message": "Updated post"
    }
    return JsonResponse(response_data)
