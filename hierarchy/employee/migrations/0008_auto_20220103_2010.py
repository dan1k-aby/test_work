# Generated by Django 2.2.19 on 2022-01-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_chief_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=15),
        ),
    ]
