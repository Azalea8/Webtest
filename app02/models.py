from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name='部门', max_length=32)

    def __str__(self):
        return self.title

class InfoUser(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0.00)
    create_time = models.DateField(verbose_name='入职时间')

    # 外键约束
    # -to:与哪张表作关联
    # -to_field: 与表中哪一列作关联
    # Django自动
    #   - 写depart
    #   - 数据列 depart_id
    # 部门表被删除
    #   联级删除
    #       depart = models.ForeignKey(verbose_name='部门ID', to='Department', to_field='id', on_delete=models.CASCADE)
    #   置空
    #       depart = models.ForeignKey(verbose_name='部门ID', to='Department', to_field='id',null=True, blank=True, on_delete=models.SET_NULL)

    depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)

    gender_choices = (
        (1, '男'),
        (0, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)

    def __str__(self):
        return self.name

class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    price = models.IntegerField(verbose_name='价格', default=0)

    level_choice = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choice, default=1)

    status_choice = (
        (1, '未占用'),
        (0, '已占用')
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choice, default=1)

class Task(models.Model):
    title = models.CharField(verbose_name='标题', max_length=64)
    detail = models.TextField(verbose_name='任务详细')

    level_choices = {
        (1, '紧急'),
        (2, '重要'),
        (3, '临时'),
    }
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)

    user = models.ForeignKey(verbose_name='负责人', to='InfoUser', to_field='id', on_delete=models.CASCADE)