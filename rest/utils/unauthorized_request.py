from django.http import HttpResponse
import json


def unauthorized_request(message=None):
    response = {"message": "Kindly login or provide a user_id query parameter"}
    if message:
        response["message"] = message
    return HttpResponse(json.dumps(response), status=401)
