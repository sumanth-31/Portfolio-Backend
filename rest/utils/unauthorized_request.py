from django.http import HttpResponse
import json


def unauthorized_request(message):
    response = {message: message}
    return HttpResponse(json.dumps(response), status=401)
