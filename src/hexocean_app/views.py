from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
