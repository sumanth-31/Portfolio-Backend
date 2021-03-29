from django.http import JsonResponse
from rest_framework.views import APIView, Request
from rest.models import User
from rest.utils import bad_request, get_user_details, unauthorized_request


class GetUser(APIView):
    def get(self, request: Request):
        user: User = request.user
        request_data = request.GET
        self_profile = request_data.get("self", None)
        if self_profile and self_profile == "true":
            if user.is_anonymous:
                return unauthorized_request("User isn't logged in. Cannot fetch self profile")
            response_data = {
                "user": get_user_details(request, user),
            }
            return JsonResponse(response_data)
        user_id = request_data.get("user_id")
        if user_id is None:
            return bad_request("user_id cannot be empty")
        try:
            user = User.objects.get(id=user_id)
        except:
            return bad_request("user not found")
        response_data = {
            "user": get_user_details(request, user)
        }
        return JsonResponse(response_data)
