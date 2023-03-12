from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from .models import Image, User
from .serializers import ImageArraySerializer, ImageSerializer, UserSerializer
from .services import create_image_array


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

    def perform_create(self, serializer):
        title = serializer.validated_data["title"]
        image = serializer.validated_data["image"]

        image_array = create_image_array(title, image, self.request.user)

        serializer.validated_data["image_array"] = image_array
        serializer.save()
