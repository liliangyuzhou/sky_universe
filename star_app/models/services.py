from django.db import models

# Create your models here.
# 如果parent为0，默认就是根节点，不再有父节点

IS_ROOT = 0


class Services(models.Model):
    name = models.CharField('name', blank=False, default='', max_length=200)
    description = models.CharField('description', blank=True, default='', max_length=1000)
    parent = models.IntegerField('父节点', blank=False, default=IS_ROOT)

    def __str__(self):
        return self.name
