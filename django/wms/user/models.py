from django.db import models


# Create your models here.
class Employee(models.Model):
    user_code = models.CharField(verbose_name='用户代码', max_length=20)
    status = models.CharField(verbose_name='用户状态', max_length=20, default='有效')
    marital = models.CharField(verbose_name='婚姻状况', max_length=15, default='未婚')
    gender = models.CharField(verbose_name='性别', max_length=2, default='男')
    id_card = models.CharField(verbose_name='身份证号', max_length=30)
    first_name = models.CharField(verbose_name="名", max_length=25)
    middle_name = models.CharField(verbose_name="中间名", max_length=25)
    last_name = models.CharField(verbose_name="姓", max_length=25)
    hire_date = models.DateField(verbose_name="入职日期")
    birth_date = models.DateField(verbose_name="出生日期")
    home_address = models.CharField(verbose_name="家庭住址", max_length=250)
    position = models.CharField(verbose_name="职位", max_length=50)
    manager_id = models.IntegerField(verbose_name="经理")
    email = models.EmailField(verbose_name="电子邮箱")
    mobile = models.CharField(verbose_name='手机号码', max_length=30)
    created_by = models.CharField(verbose_name='创建人', max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_updated_by = models.CharField(verbose_name='最后更新人', max_length=50)
    last_updated_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)
    department = models.ForeignKey('Department',on_delete=models.CASCADE)


class Department(models.Model):
    department_name = models.CharField(verbose_name='部门名称', max_length=100)
    department_desc = models.CharField(verbose_name='部门描述', max_length=300)
    supervisor = models.CharField(verbose_name='部门主管', max_length=50)
    created_by = models.CharField(verbose_name='创建人', max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_updated_by = models.CharField(verbose_name='最后更新人', max_length=50)
    last_updated_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)
