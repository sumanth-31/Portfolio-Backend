from django.http import JsonResponse
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import User, Project
from rest.utils import bad_request


class UploadProjectImage(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        user: User = request.user
        project = request.POST.get("project")
        image = request.FILES.get("project_image")
        if project is None or image is None:
            return bad_request("project and image cannot be empty")
        try:
            project_obj: Project = Project.objects.get(id=project, user=user)
        except:
            return bad_request("Project not found")
        project_obj.image = image
        project_obj.save()
        response_data = {
            "project": {
                "id": project_obj.id,
                "name": project_obj.name,
                "description": project_obj.description,
                "link": project_obj.link,
                "image": request.build_absolute_uri(project_obj.image.url)
            },
            "message": "Image upload successful"
        }
        return JsonResponse(response_data)
