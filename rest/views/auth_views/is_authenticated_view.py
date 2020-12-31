import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(["GET"])
def is_authenticated(request):
    print(request.user)
    response_data = {"authenticated": False}
    if request.user.is_anonymous:
        return HttpResponse(json.dumps(response_data), "application/json")
    response_data["authentication"] = True
    return HttpResponse(json.dumps(response_data), "application/json")
