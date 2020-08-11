from django.db import models
from django.core import serializers
import json

# Create your models here.
# 如果parent为0，默认就是根节点，不再有父节点

IS_ROOT = 0


class Services(models.Model):
    name = models.CharField('name', blank=False, default='', max_length=200)
    description = models.CharField('description', blank=True, default='', max_length=1000)
    parent = models.IntegerField('父节点', blank=False, default=IS_ROOT)

    def __str__(self):
        return self.name


    def serializers_json(self,field):
        """
        序列化成json对象
        :param field:
        :return:
        """
        data_json=serializers.serialize('json',self,field=field)
        return data_json

    def serializers_dict(self,field):
        """
        反序列化为字典
        :param field:
        :return:
        """
        data_json=self.serializers_json(field=field)
        data_dict=json.load(data_json)
        return data_dict


