from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


class CollectionView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    from ._delete import delete
    from ._get import get
