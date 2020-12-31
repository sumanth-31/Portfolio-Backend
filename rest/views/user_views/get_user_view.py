import json
from django.http import HttpResponse
from rest.models import User


def get_user(request):
    user = User.objects.first()
    profile_pic_url = request.build_absolute_uri("")
    if user.profile_pic:
        profile_pic_url = request.build_absolute_uri(user.profile_pic.url)
    resume_url = request.build_absolute_uri("")
    if resume_url:
        request.build_absolute_uri(user.resume.url)
    response_data = {
        "user": {
            "name": user.name,
            "email": user.email,
            "image": profile_pic_url,
            "resume": resume_url,
        }
    }
    return HttpResponse(json.dumps(response_data), "application/json")
