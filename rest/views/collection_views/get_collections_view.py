import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import Page, Paginator

from rest.models import Collection, Post


def get_collections(request):
    if request.method != "GET":
        return HttpResponseBadRequest("", "application/json")
    tag = request.GET.get("tag")
    # if tag is None:
    #     response_data = {"message": "Tag cannot be empty"}
    #     return HttpResponseBadRequest(json.dumps(response_data), "application/json")
    page = 1
    per_page = 10
    request_data = request.GET
    if request_data.get("page"):
        page = request_data["page"]
    if request_data.get("per_page"):
        per_page = request_data["per_page"]
    if tag:
        collections = (
            Post.objects.filter(tag=tag)
            .values("collection")
            .order_by("collection")  # collection is post object to delete specific
        )
    else:
        collections = Collection.objects.all().order_by(
            "name"
        )  # collection is collection obj to cascade delete
    print(collections)
    paginator: Paginator = Paginator(collections, per_page)
    page_obj: Page = paginator.get_page(page)
    query_collections = []
    for post in page_obj.object_list:
        image_url = ""
        collection_obj = post  # Here post is collection obj
        if tag:
            collection_obj = Collection.objects.get(
                name=post["collection"]
            )  # Here post is post obj
        if collection_obj.image:
            image_url = collection_obj.image.url
        image_url = request.build_absolute_uri(image_url)
        curr_collection = {
            "name": collection_obj.name,
            "image": image_url,
        }
        query_collections.append(curr_collection)
    meta = {
        "currPage": page_obj.number,
        "pages_count": paginator.num_pages,
        "items_count": paginator.count,
    }
    response_data = {"collections": query_collections, "meta": meta}
    return HttpResponse(json.dumps(response_data), "application/json")
