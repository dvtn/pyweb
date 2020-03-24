# Generated by Django 3.0 on 2020-03-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_department_education_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_by',
            field=models.CharField(default='管理员', max_length=50, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='department',
            name='last_updated_by',
            field=models.CharField(max_length=50, null=True, verbose_name='最后更新人'),
        ),
        migrations.AlterField(
            model_name='department',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='最后更新时间'),
        ),
        migrations.AlterField(
            model_name='education',
            name='created_by',
            field=models.CharField(default='管理员', max_length=50, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='education',
            name='last_updated_by',
            field=models.CharField(max_length=50, null=True, verbose_name='最后更新人'),
        ),
        migrations.AlterField(
            model_name='education',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='最后更新时间'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_by',
            field=models.CharField(default='管理员', max_length=50, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_updated_by',
            field=models.CharField(max_length=50, null=True, verbose_name='最后更新人'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='最后更新时间'),
        ),
    ]
