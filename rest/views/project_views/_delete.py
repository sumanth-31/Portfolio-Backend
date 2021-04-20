from rest.models import Project
from rest_framework.request import Request
from rest.utils import bad_request
from django.http import JsonResponse


def delete(self, request: Request):
    request_data = request.data
    project_id = request_data.get("project_id")
    if project_id is None:
        return bad_request("project_id cannot be empty")
    project_list = Project.objects.filter(id=project_id)
    if not project_list:
        return bad_request("No such project exists!")
    project_list[0].delete()
    response = {"message": "Deletion Successful"}
    return JsonResponse(response)
