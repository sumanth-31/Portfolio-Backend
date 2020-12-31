import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest.models import Project


class AddProject(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: HttpRequest):
        project_data = request.POST
        name = project_data.get("name")
        description = project_data.get("description")
        link = project_data.get("link")
        image = request.FILES.get("image")
        if name and description and link and image:
            project = Project(
                name=name, description=description, link=link, image=image
            )
            project.save()
            resposne_data = {
                "project": {
                    "name": name,
                    "description": description,
                    "link": link,
                    "image": request.build_absolute_uri(project.image.url),
                }
            }
            return HttpResponse(json.dumps(resposne_data), "application/json")
        else:
            return HttpResponseBadRequest(
                "name,description,link,image cannot be empty", "application/json"
            )
