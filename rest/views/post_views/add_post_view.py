import json
from django.http import JsonResponse

# Create your views here.
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest.models import Post, Collection, Tag, User
from rest.utils import bad_request, object_to_dictionary
from rest.constants import *  # pylint: disable=unused-wildcard-import


class AddPost(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request: Request):
        user: User = request.user
        payload = json.loads(request.body)
        collection = payload.get("collection", DEFAULT_COLLECTION)
        tag = payload.get("tag", DEFAULT_TAG)
        privacy = payload.get("privacy", DEFAULT_PRIVACY)
        content = payload.get("content")
        title = payload.get("title")
        if content is None:
            return bad_request("Content of post cannot be empty")
        if privacy not in PRIVACY_CLASSES:
            return bad_request("invalid privacy value")
        if title is None:
            title = ""
        collection_obj = Collection.objects.get_or_create(
            name=collection, user=user)[0]
        tag_obj = Tag.objects.get_or_create(name=tag, user=user)[0]
        post = Post(user=user,
                    content=content, collection=collection_obj, tag=tag_obj, privacy=privacy, title=title
                    )
        post.save()
        dictionary_post = object_to_dictionary(post)
        response_data = {
            "post": dictionary_post,
            "message": "Added post"
        }
        return JsonResponse(response_data)
