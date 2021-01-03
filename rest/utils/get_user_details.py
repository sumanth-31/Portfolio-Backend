from rest.models import User
from rest.utils import get_absolute_uri


def get_user_details(request, user: User):
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
