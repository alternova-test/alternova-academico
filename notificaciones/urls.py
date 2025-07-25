from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificacionViewSet

router = DefaultRouter()
router.register('notificaciones', NotificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
