from .views import DocumentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Docs', DocumentViewSet)

urlpatterns = [] + router.urls
