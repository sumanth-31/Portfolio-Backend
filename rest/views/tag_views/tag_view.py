from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


class TagView(APIView):
    from ._get import get
    from ._delete import delete
