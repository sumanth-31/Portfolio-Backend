from django.http import JsonResponse
from django.core.paginator import Page, Paginator
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import Tag, User
from rest.utils import meta_details_generator


class GetTags(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        user: User = request.user
        request_data = request.GET
        search_query = request_data.get("search_query", None)
        tags = Tag.objects.filter(user=user)
        if search_query:
            tags = tags.filter(name__icontains=search_query)
        query_tags = []
        for tag in tags:
            curr_tag = {
                "name": tag.name,
                "id": tag.id
            }
            if tag.image:
                image_url_raw = tag.image.url
                image_url = request.build_absolute_uri(image_url_raw)
                curr_tag["image"] = image_url
            query_tags.append(curr_tag)
        response_data = {"tags": query_tags}
        return JsonResponse(response_data)
