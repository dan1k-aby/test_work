from rest_framework import serializers
from .models import Employee, Chief
from rest_framework.relations import SlugRelatedField


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee

class ChiefSerializer(serializers.ModelSerializer):
    full_name_chief = SlugRelatedField(slug_field='full_name', queryset=Employee.objects.all())
    full_name_employee = SlugRelatedField(slug_field='full_name', queryset=Employee.objects.all())
    employee_position = SlugRelatedField(slug_field='position', read_only=True)
    
    class Meta:
        fields = "__all__"
        model = Chief