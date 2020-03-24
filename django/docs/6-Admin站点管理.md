Admin站点管理
---
[toc]

# 1.概述
Admin站点管理主要用来做后台管理，用来做内容发布与公告访问，负责添加，修改和删除内容。

# 2.配置Admin应用

## 2.1.注册admin模块
在settings.py文件中的INSTALLED_APPS中添加'django.contrib.admin', 默认是添加好的。

## 2.2.创建后台超级管理员

```bash
$ python manage.py createsuperuser 
Username (leave blank to use 'david.tian'): david.tian
Email address: david.tian@live.com
Password: 
Password (again): 
Superuser created successfully.
```

## 2.3.汉化
在settings.py中配置下面两个选项，注册原有项，然后重启服务，刷新原有站点管理页面。

```python
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
```

## 2.4.管理数据表
修改admin.py文件