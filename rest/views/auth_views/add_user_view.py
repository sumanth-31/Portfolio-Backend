import json
from django.http import JsonResponse

# Create your views here.

from rest.models import User
from rest.utils import object_to_dictionary,bad_request
from rest.views import APIView

class AddUser(APIView):
    def post(self,request):
        data = json.loads(request.body)
        name = data["name"]
        password = data["password"]
        email = data["email"]
        if User.objects.filter(email=email).exists():   #user exists
            return bad_request("User already exists!")
        user = User.objects.create_user(name=name, email=email, password=password)
        response_data=object_to_dictionary(user)
        return JsonResponse(response_data)
