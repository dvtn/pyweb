# Generated by Django 3.0 on 2020-03-24 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0010_auto_20200324_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, verbose_name='部门名称')),
                ('department_desc', models.CharField(max_length=300, verbose_name='部门描述')),
                ('supervisor', models.CharField(max_length=50, verbose_name='部门主管')),
                ('created_by', models.CharField(default='管理员', max_length=50, verbose_name='创建人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_by', models.CharField(default='管理员', max_length=50, null=True, verbose_name='最后更新人')),
                ('last_updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '部门表',
                'verbose_name_plural': '部门表',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=200, verbose_name='毕业院校')),
                ('created_by', models.CharField(default='管理员', max_length=50, verbose_name='创建人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_by', models.CharField(default='管理员', max_length=50, null=True, verbose_name='最后更新人')),
                ('last_updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '教育表',
                'verbose_name_plural': '教育表',
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.CharField(max_length=20, verbose_name='用户代码')),
                ('user_name', models.CharField(max_length=50, verbose_name='用户姓名')),
                ('nation', models.CharField(choices=[('han', '汉族'), ('menggu', '蒙古族'), ('tujia', '土家族'), ('zhuang', '壮族'), ('manchu', '满族'), ('hui', '回族'), ('miao', '苗族'), ('uyghur', '维族'), ('tibetan', '藏族'), ('yi', '彝簇'), ('others', '其它')], max_length=10, verbose_name='民族')),
                ('status', models.CharField(choices=[('incumbency', '在职'), ('resignation', '离职')], max_length=20, verbose_name='用户状态')),
                ('marital', models.CharField(choices=[('married', '已婚'), ('unmarried', '未婚'), ('divorce', '离异')], default='未婚', max_length=15, verbose_name='婚姻状况')),
                ('gender', models.CharField(choices=[('F', '女'), ('M', '男')], default='男', max_length=2, verbose_name='性别')),
                ('id_card', models.CharField(max_length=30, verbose_name='身份证号')),
                ('hire_date', models.DateField(verbose_name='入职日期')),
                ('birth_date', models.DateField(verbose_name='出生日期')),
                ('home_address', models.CharField(max_length=250, verbose_name='家庭住址')),
                ('position', models.CharField(max_length=50, verbose_name='职位')),
                ('manager_id', models.IntegerField(verbose_name='经理')),
                ('email', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('mobile', models.CharField(max_length=30, verbose_name='手机号码')),
                ('education', models.CharField(choices=[('colleage', '大学'), ('high', '高中'), ('junior', '初中'), ('primary', '小学')], default='大学', max_length=50, verbose_name='学历')),
                ('degree', models.CharField(choices=[('doctor', '博士'), ('master', '硕士研究生'), ('bachelor', '学士'), ('other', '其它')], default='学士', max_length=50, verbose_name='学位')),
                ('major', models.CharField(max_length=50, verbose_name='专业')),
                ('enrollment_date', models.DateField(verbose_name='入学时间')),
                ('graduate_date', models.DateField(verbose_name='毕业时间')),
                ('created_by', models.CharField(default='管理员', max_length=50, verbose_name='创建人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_updated_by', models.CharField(default='管理员', max_length=50, null=True, verbose_name='最后更新人')),
                ('last_updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='最后更新时间')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Department')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Education')),
            ],
            options={
                'verbose_name': '员工信息表',
                'verbose_name_plural': '员工信息表',
                'db_table': 'employee',
            },
        ),
    ]
