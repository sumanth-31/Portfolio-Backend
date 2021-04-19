from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


class ProjectView(APIView):
    from ._get import get
    from ._post import post
    from ._put import put
