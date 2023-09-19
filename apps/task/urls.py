from django.urls import path
from rest_framework import routers

from apps.task.views import TaskViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register("task", TaskViewSet)
router.register("category", CategoryViewSet)
urlpatterns = router.urls
