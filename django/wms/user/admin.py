from django.contrib import admin

# Register your models here.
from .models import Employee, Department, Education


class EmployeeAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = ['pk', 'user_code', 'user_name', 'status', 'marital', 'gender', 'id_card', 'hire_date', 'birth_date',
                    'home_address', 'position', 'manager_id', 'email', 'mobile',
                    'created_by', 'last_updated_by']  # 显示字段
    list_filter = ['status', 'marital']  # 过滤器
    search_fields = ['user_code', 'email', 'position']  # 搜索字段
    list_per_page = 20  # 分页
    # # 添加,修改页属性 (fields与fieldsets不能同时使用)
    # fields = [] # 属性的先后顺序
    # fieldsets = [] # 属性分组
    fieldsets = [
        ('员工基本信息', {'fields': ['user_code', 'user_name', 'gender', 'marital', 'id_card',
                               'birth_date', 'mobile', 'home_address']}),
        ('职位信息', {'fields': ['department', 'manager_id', 'email', 'position', 'hire_date', 'status', 'created_by',
                             'last_updated_by']}),
        ('教育背景',{'fields':['education','degree','major','enrollment_date','graduate_date']})
    ]


# 注册
admin.site.register(Employee, EmployeeAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'department_name', 'department_desc', 'supervisor', 'created_by', 'created_time',
                    'last_updated_by', 'last_updated_by']
    list_filter = ['department_name', 'supervisor']
    search_fields = ['department_name', 'supervisor']
    list_per_page = 15


admin.site.register(Department, DepartmentAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'created_by', 'created_time',
                    'last_updated_by', 'last_updated_by']
    list_filter = ['institution']
    search_fields = ['institution']
    list_per_page = 15


admin.site.register(Education, EducationAdmin)
