# Generated by Django 3.0.8 on 2020-08-15 12:07

from django.db import migrations, models
import django.db.models.deletion
import star_app.models.base
import star_app.models.object_field


class Migration(migrations.Migration):

    dependencies = [
        ('star_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField(default='', max_length=500, verbose_name='description')),
                ('host', models.CharField(default='', max_length=200, verbose_name='host')),
                ('url', models.CharField(max_length=500, verbose_name='url')),
                ('method', models.CharField(max_length=20, verbose_name='method')),
                ('headers', star_app.models.object_field.ObjectField(default={}, verbose_name='headers')),
                ('parameter', star_app.models.object_field.ObjectField(default={}, verbose_name='parameter')),
                ('parameter_type', models.CharField(default='json', max_length=20, verbose_name='parameter_type,json or form')),
                ('response', star_app.models.object_field.ObjectField(default='', verbose_name='response')),
                ('response_type', models.CharField(default='json', max_length=20, verbose_name='parameter_type,json or form')),
                ('asserts', star_app.models.object_field.ObjectField(default=[], verbose_name='asserts')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_interface', to='star_app.Services')),
            ],
            bases=(models.Model, star_app.models.base.Base),
        ),
    ]
