import json
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from rest.models import User


@csrf_exempt
def add_user(request):
    data = json.loads(request.body)
    name = data["name"]
    password = data["password"]
    email = data["email"]
    user = User.objects.create_user(name=name, email=email, password=password)
    data = serializers.serialize("json", [user,])
    return HttpResponse(data, content_type="application/json")
