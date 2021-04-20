import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.request import Request
# Create your views here.
from rest.utils import bad_request
from rest.convertors import user_to_json


class Login(APIView):
    def post(self, request: Request):
        user_data = request.data
        email = user_data.get("email")
        password = user_data.get("password")
        user = authenticate(email=email, password=password)
        if user is None:
            return bad_request("Invalid credentials")
        response_data = {"user": user_to_json(
            request, user), "token": user.token}
        return JsonResponse(response_data)
