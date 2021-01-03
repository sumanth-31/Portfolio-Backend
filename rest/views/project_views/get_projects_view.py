from django.http import JsonResponse
from django.core.paginator import Paginator, Page
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import User, Project


class GetProjects(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        user: User = request.user
        page = request.POST.get("page", 1)
        per_page = request.POST.get("per_page", 10)
        project_objects = Project.objects.all().filter(user=user)
        paginator = Paginator(project_objects, per_page)
        page_obj: Page = paginator.get_page(page)
        project_list = []
        for project in page_obj.object_list:
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
            project_list.append(curr_project)
        response_data = {
            "projects": project_list
        }
        return JsonResponse(response_data)
