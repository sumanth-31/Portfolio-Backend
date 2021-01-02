from django.http import JsonResponse
from django.core.paginator import Page, Paginator
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import Tag, User


class GetTags(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        user: User = request.user
        page = 1
        per_page = 10
        request_data = request.GET
        if request_data.get("page"):
            page = request_data["page"]
        if request_data.get("per_page"):
            per_page = request_data["per_page"]
        tags = Tag.objects.filter(user=user)
        paginator: Paginator = Paginator(tags, per_page)
        page_obj: Page = paginator.get_page(page)
        query_tags = []
        for tag in page_obj.object_list:
            curr_tag = {
                "name": tag.name,
                "id": tag.id
            }
            if tag.image:
                image_url_raw = tag.image.url
                image_url = request.build_absolute_uri(image_url_raw)
                curr_tag["image"] = image_url
            query_tags.append(curr_tag)
        meta = {
            "currPage": page_obj.number,
            "pages_count": paginator.num_pages,
            "items_count": paginator.count,
        }
        response_data = {"tags": query_tags, "meta": meta}
        return JsonResponse(response_data)
