# Generated by Django 3.0 on 2020-03-24 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_department_education_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='education',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
