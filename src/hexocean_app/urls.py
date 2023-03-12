from django.urls import path
from rest_framework import routers

from .views import ImageArrayViewSet, ImageViewSet, UserViewSet, redirect_view

router = routers.DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("images", ImageViewSet, basename="images")
router.register("image-arrays", ImageArrayViewSet, basename="image-arrays")

urlpatterns = router.urls

urlpatterns.append(
    path("redirect/<str:expiry_token>/", redirect_view, name="redirect"),
)
