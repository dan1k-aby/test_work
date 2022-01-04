from django.contrib import admin
from .models import Employee, Chief

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 
                    'employment_date', 'salary')
    
    search_fields = ('full_name',)
    list_filter = ('employment_date',)

class ChiefAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_chief', 'full_name_employee')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Chief, ChiefAdmin)