# Generated by Django 3.0.8 on 2020-08-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_app', '0005_auto_20200824_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfaceresult',
            name='success',
            field=models.BooleanField(default=False, verbose_name='测试结果'),
        ),
    ]