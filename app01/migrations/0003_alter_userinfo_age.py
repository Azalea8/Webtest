# Generated by Django 3.2.4 on 2023-05-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]