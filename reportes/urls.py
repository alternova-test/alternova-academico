from django.urls import path
from .views import promedio_estudiante

urlpatterns = [
    path('promedio/<int:estudiante_id>/', promedio_estudiante),
]