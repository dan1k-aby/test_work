from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()

router_v1.register(r'employeer', views.EmployeeViewSet, basename="employee")
router_v1.register(r'chief', views.ChiefViewSet, basename='chiefs')

urlpatterns = [
    path('', include(router_v1.urls)),
]