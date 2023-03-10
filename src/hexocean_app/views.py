from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from .models import Image, ImageArray, User
from .serializers import ImageArraySerializer, ImageSerializer, UserSerializer


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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return user.image_arrays.all()
