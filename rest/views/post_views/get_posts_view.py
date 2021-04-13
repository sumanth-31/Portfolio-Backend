from django.http import JsonResponse
from django.core.paginator import Paginator, Page

# Create your views here.
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated

from rest.models import Post, User
from rest.utils import object_to_dictionary, meta_details_generator


class GetPosts(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        user: User = request.user
        request_data = request.GET
        page = request_data.get("page", 1)
        per_page = request_data.get("per_page", 10)
        collection = request_data.get("collection")
        tag = request_data.get("tag")
        search_query = request_data.get("search_query", "")
        posts = Post.objects.all().filter(user=user, title__icontains=search_query)
        if collection is not None:
            posts = posts.filter(collection=collection)
        if tag is not None:
            posts = posts.filter(tag=tag)
        paginator: Paginator = Paginator(posts, per_page)
        page_obj: Page = paginator.get_page(page)
        query_posts = []
        for post in page_obj.object_list:
            curr_post = object_to_dictionary(post)
            query_posts.append(curr_post)
        meta = meta_details_generator(
            page_obj.number, paginator.num_pages, paginator.count)
        response_data = {"posts": query_posts, "meta": meta}
        return JsonResponse(response_data)
