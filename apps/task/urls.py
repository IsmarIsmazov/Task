from django.urls import path
from rest_framework import routers

from apps.task.views import TaskViewSet

router = routers.DefaultRouter()
router.register("task", TaskViewSet)
urlpatterns = router.urls
