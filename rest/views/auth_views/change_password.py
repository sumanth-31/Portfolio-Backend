import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.request import Request


class ChangePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        user = request.user
        request_data = request.data
        user.set_password(request_data.get("password"))
        user.save()
        return HttpResponse("Password Changed", "application/json")
