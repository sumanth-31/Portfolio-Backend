from django.http import JsonResponse
from rest_framework.views import Request
from rest.models import Project, User
from rest.utils import bad_request
from rest.convertors import project_to_json


def post(self, request: Request):
    user: User = request.user
    project_data = request.POST
    name = project_data.get("name")
    description = project_data.get("description")
    link = project_data.get("link")
    image = request.FILES.get("image")
    if name and description and link:
        project = Project(
            name=name, description=description, link=link, image=image, user=user
        )
        project.save()
        response_project = project_to_json(request, project)
        response_data = {"project": response_project}
        return JsonResponse(response_data)
    else:
        return bad_request("name,description,link cannot be empty")
