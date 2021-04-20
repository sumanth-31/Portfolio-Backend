from rest.models import Project
from rest_framework.request import Request


def project_to_json(request: Request, project: Project):
    project_json = {
        "id": project.id,
        "name": project.name,
        "link": project.link,
        "description": project.description
    }
    if project.image:
        image_url_raw = project.image.url
        project_json["image"] = request.build_absolute_uri(
            image_url_raw)
    return project_json
