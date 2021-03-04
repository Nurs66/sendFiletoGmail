from rest_framework.routers import DefaultRouter
from sms_sender.views import PersonViewSet


router = DefaultRouter()
router.register(r"", PersonViewSet, basename='person')

urlpatterns = router.urls
