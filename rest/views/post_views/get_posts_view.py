from django.http import JsonResponse
from django.core.paginator import Paginator, Page

# Create your views here.
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated

from rest.models import Post, User
from rest.utils import meta_details_generator, bad_request, unauthorized_request, invalid_user
from rest.convertors import post_to_json


class GetPosts(APIView):

    def get(self, request: Request):
        user: User = request.user
        request_data = request.GET
        post_id = request_data.get("post_id", None)
        user_id = request_data.get("user_id", None)
        if user_id:
            user_list = User.objects.all().filter(id=user_id)
            if not user_list:
                return invalid_user()
            user = user_list[0]
        posts = Post.objects.all()
        if post_id:
            post_list = posts.filter(post_id=post_id)
            if not post_list:
                return bad_request("No Such Post Exists!")
            response_data = {
                "post": post_to_json(post_list[0])
            }
            return JsonResponse(response_data)
        if user.is_anonymous:
            return unauthorized_request()
        userPosts = posts.filter(user=user)
        page = request_data.get("page", 1)
        per_page = request_data.get("per_page", 10)
        collection = request_data.get("collection")
        tag = request_data.get("tag")
        search_query = request_data.get("search_query", "")
        posts = userPosts.filter(title__icontains=search_query)
        if collection is not None:
            posts = posts.filter(collection=collection)
        if tag is not None:
            posts = posts.filter(tag=tag)
        paginator: Paginator = Paginator(posts, per_page)
        page_obj: Page = paginator.get_page(page)
        query_posts = []
        for post in page_obj.object_list:
            curr_post = post_to_json(post)
            query_posts.append(curr_post)
        meta = meta_details_generator(
            page_obj.number, paginator.num_pages, paginator.count)
        response_data = {"posts": query_posts, "meta": meta}
        return JsonResponse(response_data)
