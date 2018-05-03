from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_api import views

router = DefaultRouter()
router.register(r'group', views.GroupViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'task', views.TaskViewSet, base_name='task')

urlpatterns = [
    url(r'^', include(router.urls)),
]