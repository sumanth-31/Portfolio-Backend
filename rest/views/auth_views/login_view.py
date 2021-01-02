import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView

# Create your views here.
from rest.utils import bad_request

class Login(APIView):
    def post(self,request):
        user_data = json.loads(request.body)
        email=user_data["email"]
        password=user_data["password"]
        user = authenticate(email=email,password=password)
        if user is None:
            return bad_request("Invalid credentials")
        response_data = {"token": user.token}
        return JsonResponse(response_data)
