# Generated by Django 2.2.19 on 2022-01-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0002_delete_voditeli'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30, verbose_name='ФИО')),
                ('position', models.CharField(max_length=15, verbose_name='Должность')),
                ('employment_date', models.DateField(verbose_name='Дата приема на работу')),
                ('salary', models.IntegerField(verbose_name='Размер заработной платы')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
