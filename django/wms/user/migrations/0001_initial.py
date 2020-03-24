# Generated by Django 3.0 on 2020-03-23 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, verbose_name='部门名称')),
                ('department_desc', models.CharField(max_length=300, verbose_name='部门描述')),
                ('supervisor', models.CharField(max_length=50, verbose_name='部门主管')),
                ('created_by', models.CharField(max_length=50, verbose_name='创建人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_by', models.CharField(max_length=50, verbose_name='最后更新人')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.CharField(max_length=20, verbose_name='用户代码')),
                ('status', models.CharField(default='有效', max_length=20, verbose_name='用户状态')),
                ('marital', models.CharField(default='未婚', max_length=15, verbose_name='婚姻状况')),
                ('gender', models.CharField(default='男', max_length=2, verbose_name='性别')),
                ('id_card', models.CharField(max_length=30, verbose_name='身份证号')),
                ('first_name', models.CharField(max_length=25, verbose_name='名')),
                ('middle_name', models.CharField(max_length=25, verbose_name='中间名')),
                ('last_name', models.CharField(max_length=25, verbose_name='姓')),
                ('hire_date', models.DateField(verbose_name='入职日期')),
                ('birth_date', models.DateField(verbose_name='出生日期')),
                ('home_address', models.CharField(max_length=250, verbose_name='家庭住址')),
                ('position', models.CharField(max_length=50, verbose_name='职位')),
                ('manager_id', models.IntegerField(verbose_name='经理')),
                ('email', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('mobile', models.CharField(max_length=30, verbose_name='手机号码')),
                ('created_by', models.CharField(max_length=50, verbose_name='创建人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_by', models.CharField(max_length=50, verbose_name='最后更新人')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Department')),
            ],
        ),
    ]