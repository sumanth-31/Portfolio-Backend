import json
from django.http import JsonResponse

# Create your views here.

from rest.models import User
from rest.utils import bad_request
from rest_framework.views import APIView
from rest_framework.request import Request
from rest.convertors import user_to_json


class AddUser(APIView):
    def post(self, request: Request):
        data = request.data
        name = data.get("name")
        password = data.get("password")
        email = data.get("email")
        if User.objects.filter(email=email).exists():  # user exists
            return bad_request("User already exists!")
        user = User.objects.create_user(
            name=name, email=email, password=password)
        response_data = user_to_json(request, user)
        return JsonResponse(response_data)
