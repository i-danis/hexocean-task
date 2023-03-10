from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import User, Image, ImageArray
from .serializers import UserSerializer, ImageSerializer, ImageArraySerializer


class UserViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ImageViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageArrayViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = ImageArraySerializer
    queryset = ImageArray.objects.all()
