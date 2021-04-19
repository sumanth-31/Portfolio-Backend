from django.http import JsonResponse
from rest_framework.views import Request
from rest.models import Project, User
from rest.utils import bad_request


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
        response_data = {
            "project": {
                "name": name,
                "description": description,
                "link": link,
                "id": project.id
            }
        }
        if image:
            response_data["image"] = request.build_absolute_uri(
                project.image.url)
        return JsonResponse(response_data)
    else:
        return bad_request("name,description,link cannot be empty")
