import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, Page

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest.models import Post, Collection, Tag

@csrf_exempt
def get_posts(request):
    if request.method != "GET":
        return HttpResponseBadRequest("", "application/json")
    page = 1
    per_page = 10
    request_data = request.GET
    if request_data.get("page"):
        page = request_data["page"]
    if request_data.get("per_page"):
        per_page = request_data["per_page"]

    if request_data.get("collection") and request_data.get("tag"):
        posts = Post.objects.filter(
            collection=request_data["collection"], tag=request_data["tag"]
        )
    else:
        posts = Post.objects.all()
    paginator: Paginator = Paginator(posts, per_page)
    page_obj: Page = paginator.get_page(page)
    query_posts = []
    for post in page_obj.object_list:
        curr_post = {
            "post_id": post.post_id,
            "content": post.content,
            "collection": post.collection.name,
            "tag": post.tag.name,
        }
        query_posts.append(curr_post)
    meta = {
        "currPage": page_obj.number,
        "pages_count": paginator.num_pages,
        "items_count": paginator.count,
    }
    response_data = {"posts": query_posts, "meta": meta}
    return HttpResponse(json.dumps(response_data), "application/json")
