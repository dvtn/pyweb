from django.db import models


# Create your models here.
class Employee(models.Model):
    STATUS = (
        ('incumbency','在职'),
        ('resignation','离职'),
    )

    MARITAL = (
        ('married','已婚'),
        ('unmarried','未婚'),
    )

    NATION = (
        ('han','汉族'),
        ('menggu','蒙古族'),
        ('tujia','土家族'),
        ('zhuang','壮族'),
        ('manchu','满族'),
        ('hui','回族'),
        ('miao','苗族'),
        ('uyghur','维族'),
        ('tibetan','藏族'),
        ('yi','彝簇'),
        ('others','其它'),
    )
    GENDER=(
        ('F','女'),
        ('M','男'),
    )

    EDUCATION = (
        ('colleage','大学'),
        ('high','高中'),
        ('junior','初中'),
        ('primary','小学'),
    )
    DEGREE = (
        ('doctor','博士'),
        ('master','硕士研究生'),
        ('bachelor','学士'),
        ('other','其它'),
    )

    user_code = models.CharField(verbose_name='用户代码', max_length=20)
    user_name = models.CharField(verbose_name='用户姓名', max_length=50)
    nation = models.CharField(verbose_name="民族", choices=NATION, max_length=10)
    status = models.CharField(verbose_name='用户状态', max_length=20, choices=STATUS)
    marital = models.CharField(verbose_name='婚姻状况', max_length=15,choices=MARITAL)
    gender = models.BooleanField(verbose_name='性别',choices=GENDER)
    id_card = models.CharField(verbose_name='身份证号', max_length=30)
    hire_date = models.DateField(verbose_name="入职日期")
    birth_date = models.DateField(verbose_name="出生日期")
    home_address = models.CharField(verbose_name="家庭住址", max_length=250)
    position = models.CharField(verbose_name="职位", max_length=50)
    manager_id = models.IntegerField(verbose_name="经理")
    email = models.EmailField(verbose_name="电子邮箱")
    mobile = models.CharField(verbose_name='手机号码', max_length=30)
    department = models.ForeignKey('Department',on_delete=models.CASCADE)
    education = models.ForeignKey('Education', on_delete=models.CASCADE)

    degree = models.CharField(verbose_name='学位', choices=DEGREE, max_length=50)
    major = models.CharField(verbose_name='专业', max_length=50)
    enrollment_date = models.DateField(verbose_name='入学时间')
    graduate_date = models.DateField(verbose_name='毕业时间')
    created_by = models.CharField(verbose_name='创建人', max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_updated_by = models.CharField(verbose_name='最后更新人', max_length=50)
    last_updated_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)

    class Meta(object):
        db_table = 'employee'
        verbose_name_plural = '员工信息表'
        verbose_name=verbose_name_plural


class Department(models.Model):
    department_name = models.CharField(verbose_name='部门名称', max_length=100)
    department_desc = models.CharField(verbose_name='部门描述', max_length=300)
    supervisor = models.CharField(verbose_name='部门主管', max_length=50)
    created_by = models.CharField(verbose_name='创建人', max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_updated_by = models.CharField(verbose_name='最后更新人', max_length=50)
    last_updated_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)

    class Meta(object):
        db_table = 'department'
        verbose_name_plural = '部门表'
        verbose_name= verbose_name_plural


class Education(models.Model):

    institution = models.CharField(verbose_name='毕业院校', max_length=200)
    created_by = models.CharField(verbose_name='创建人', max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_updated_by = models.CharField(verbose_name='最后更新人', max_length=50)
    last_updated_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)

    class Meta(object):
        db_table = 'education'
        verbose_name_plural = '教育表'
        verbose_name= verbose_name_plural
