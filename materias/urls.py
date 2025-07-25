from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MateriaViewSet, NotaViewSet

router = DefaultRouter()
router.register('materias', MateriaViewSet)
router.register('notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]