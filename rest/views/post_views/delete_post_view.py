import json
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest.models import Post


class DeletePost(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        post_id = request.GET.get("post_id")
        if post_id is None:
            response_data = {"message": "post_id cannot be empty"}
            return HttpResponseBadRequest(json.dumps(response_data), "application/json")
        post = None
        try:
            post = Post.objects.get(post_id=post_id)
        except:
            response_data = {"message": "post not found"}
            return HttpResponseBadRequest(json.dumps(response_data), "application/json")
        post.delete()
        response_data = {"post_id": post_id, "message": "Post successfully Deleted"}
        return HttpResponse(json.dumps(response_data), "application/json")
