from rest_framework import routers

from apps.task.views import TaskViewSet

router = routers.DefaultRouter()
router.register("users", TaskViewSet)
urlpatterns = router.urls