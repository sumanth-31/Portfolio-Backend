import json
from django.http import HttpResponseBadRequest

def bad_request(message):
    response={"message":message}
    return HttpResponseBadRequest(json.dumps(response),"application/json")
