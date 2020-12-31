import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse


class ChangePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        request_data = json.loads(request.body)
        user.set_password(request_data.get("password"))
        user.save()
        return HttpResponse("Password Changed", "application/json")
