from rest_framework import routers

from .views import UserViewSet, ImageViewSet, ImageArrayViewSet

router = routers.DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("images", ImageViewSet, basename="images")
router.register("image-arrays", ImageArrayViewSet, basename="image-arrays")

urlpatterns = router.urls
