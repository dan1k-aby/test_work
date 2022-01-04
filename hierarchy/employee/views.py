from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Employee, Chief
from .serializers import EmployeeSerializer, ChiefSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    filterset_fields = ('full_name', 'position', 'employment_date', 'salary',)
    search_fields = ('full_name', 'position', 'employment_date', 'salary',)
    ordering_fields = ('full_name', 'position', 'employment_date', 'salary',)

class ChiefViewSet(viewsets.ModelViewSet):
    queryset = Chief.objects.all()
    serializer_class = ChiefSerializer

