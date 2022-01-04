from django.db import models


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=30)
    position = models.CharField('Должность', max_length=15)
    employment_date = models.DateField('Дата приема на работу')
    salary = models.IntegerField('Размер заработной платы')

    class Meta:
        ordering = ('id',)

class Chief(models.Model):
    full_name_chief = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='chief', null=True
    )
    full_name_employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='chief_employee', null=True
    )
    employee_position = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='chief_employee_position', null=True
    )

    class Meta:
        ordering = ('id',)