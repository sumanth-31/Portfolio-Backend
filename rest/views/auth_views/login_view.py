import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your views here.


@csrf_exempt
def login(request):
    if request.method != "POST":
        return HttpResponseBadRequest("", content_type="application/json")
    user_data = json.loads(request.body)
    user = authenticate(username=user_data["email"], password=user_data["password"])
    if user is None:
        return HttpResponse("Invalid credentials", "application/json", status=422)
    response_data = json.dumps({"token": user.token})
    return HttpResponse(response_data, "application/json")
