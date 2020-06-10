# {{ app_name }}/urls.py
from rest_framework.routers import DefaultRouter

from .views import {{ single_app_name }}ViewSet


router = DefaultRouter(trailing_slash=False)
router.register("items", {{ single_app_name }}ViewSet)

urlpatterns = router.urls
