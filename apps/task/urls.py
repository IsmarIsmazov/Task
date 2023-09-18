from django.urls import path
from rest_framework import routers

from apps.task.views import TaskViewSet, HashtagViewSet

router = routers.DefaultRouter()
router.register("task", TaskViewSet)
router.register("hashtag", HashtagViewSet)
urlpatterns = router.urls
