from django.http import JsonResponse
from django.core.paginator import Paginator, Page
from rest_framework.views import APIView, Request
from rest_framework.permissions import IsAuthenticated
from rest.models import User, Project
from rest.utils import meta_details_generator
from rest.utils import bad_request, unauthorized_request


class GetProjects(APIView):
    def get(self, request: Request):
        user: User = request.user
        project_id = request.GET.get("project_id", None)
        page = request.GET.get("page", 1)
        per_page = request.GET.get("per_page", 10)
        user_id = request.GET.get("user_id", None)
        if user_id:  # projects of specific users are requested
            user_list = User.objects.all().filter(id=user_id)
            if not user_list:
                return bad_request("No Such User Exists!")
            user = user_list[0]
        # If project_id is not there and user isn't logged in or specified, we don't know which user's projects are requested
        if (not project_id) and user.is_anonymous:
            return unauthorized_request("Kindly login or provide a user_id query parameter")
        project_objects = Project.objects.all()
        if not user.is_anonymous:
            project_objects = project_objects.filter(user=user)
        if (project_id):
            projectSet = project_objects.filter(id=project_id)
            if not projectSet:
                return bad_request("No Such Project Exists!")
            project = projectSet[0]
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
            response_data = {"project": curr_project}
            return JsonResponse(response_data)
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
        meta = meta_details_generator(
            page_obj.number, paginator.num_pages, paginator.count)
        response_data = {
            "projects": project_list,
            "meta": meta
        }
        return JsonResponse(response_data)
