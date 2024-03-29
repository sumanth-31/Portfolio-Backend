from django.http import JsonResponse
from rest_framework.views import Request
from rest.models import User, Project
from rest.utils import bad_request
import json


def put(self, request: Request):
    user: User = request.user
    request_data = request.data
    project_id = request_data.get("project_id", None)
    if (project_id == None):
        return bad_request("project_id cannot be empty")
    name = request_data.get("name", None)
    link = request_data.get("link", None)
    description = request_data.get("description", None)
    image = request.FILES.get("image")
    project_list = Project.objects.filter(user=user, id=project_id)
    if not project_list:
        return bad_request("No Such Project Exists!")
    project: Project = project_list[0]
    if name:
        project.name = name
    if link:
        project.link = link
    if description:
        project.description = description
    if image:
        project.image = image
    project.save()
    curr_project = {
        "id": project.id,
        "name": project.name,
        "link": project.link,
        "description": project.description
    }
    if project.image:
        image_url_raw = project.image.url
        curr_project["image"] = request.build_absolute_uri(
            image_url_raw)
    response_data = {
        "project": curr_project,
        "message": "Project Successfully Updated!"
    }
    return JsonResponse(response_data)
