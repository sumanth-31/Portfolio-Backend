import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import Page, Paginator

from rest.models import Tag, Post


def get_tags(request):
    if request.method != "GET":
        return HttpResponseBadRequest("", "application/json")
    collection = request.GET.get("collection")
    page = 1
    per_page = 10
    request_data = request.GET
    if request_data.get("page"):
        page = request_data["page"]
    if request_data.get("per_page"):
        per_page = request_data["per_page"]
    if collection is None:
        tags = Tag.objects.all().order_by(
            "name"
        )  # Tag is a tag instance, to delete all posts with tag using cascade
    else:
        tags = (
            Post.objects.filter(collection=collection).values("tag").order_by("tag")
        )  # Tag is a post if collection is mentioned, to delete specified
    paginator: Paginator = Paginator(tags, per_page)
    page_obj: Page = paginator.get_page(page)
    query_tags = []
    for tag in page_obj.object_list:
        image_url = ""
        tag_obj = tag  # Here tag is tag obj
        if collection:
            tag_obj = Tag.objects.get(name=tag["tag"])  # Here tag is post obj
        if tag_obj.image:
            image_url = tag.image.url
        image_url = request.build_absolute_uri(image_url)
        curr_tag = {
            "name": tag_obj.name,
            "image": image_url,
        }
        query_tags.append(curr_tag)
    meta = {
        "currPage": page_obj.number,
        "pages_count": paginator.num_pages,
        "items_count": paginator.count,
    }
    response_data = {"tags": query_tags, "meta": meta}
    return HttpResponse(json.dumps(response_data), "application/json")
