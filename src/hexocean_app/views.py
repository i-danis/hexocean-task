import redis
from django.shortcuts import redirect
from rest_framework import mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Image, User
from .serializers import ImageArraySerializer, ImageSerializer, UserSerializer
from .services import create_expiration_link, create_image_array


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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        image_arrays = user.image_arrays.all()
        images = Image.objects.filter(image_array__in=image_arrays)
        return images

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer_data = serializer.data
        expiration_time = request.query_params.get("expiration_time")
        if request.user.tier.is_expiration_link and expiration_time:
            expiration_time = int(expiration_time)
            if expiration_time < 300 or expiration_time > 30_000:
                return Response(
                    data={"message": "expiration_time should be between 300 and 30000"},
                    status=400,
                )
            expiration_link = create_expiration_link(
                serializer_data["content"], expiration_time
            )

            serializer_data.update({"expiration_link": expiration_link})

        return Response(serializer_data)


@api_view(["GET"])
def redirect_view(request, expiry_token):
    r = redis.Redis(host="redis", port=6379)
    original_link = r.get(expiry_token)
    if original_link:
        original_link = original_link.decode()
        return redirect(original_link)

    return Response(data={"message": "link is expired"}, status=404)


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
