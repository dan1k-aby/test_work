# Generated by Django 2.2.19 on 2022-01-03 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20220102_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='chief',
            name='employee_position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chief_employee_position', to='employee.Employee'),
        ),
    ]