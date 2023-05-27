# Generated by Django 3.2.4 on 2023-05-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_auto_20230516_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('price', models.IntegerField(default=0, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级'), (4, '四级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(1, '未占用'), (0, '已占用')], default=1, verbose_name='状态')),
            ],
        ),
    ]
