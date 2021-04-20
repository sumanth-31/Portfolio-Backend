from rest_framework.request import Request
from rest.models import User
from rest.utils import get_absolute_uri


def user_to_json(request: Request, user: User):
    user_data = {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }
    if user.resume:
        user_data["resume"] = get_absolute_uri(request, user.resume)
    if user.profile_pic:
        user_data["image"] = get_absolute_uri(request, user.profile_pic)
    return user_data
