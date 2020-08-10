# coding=utf-8
# @Time    : 2020/8/5 6:57 下午
# @Author  : liliang
# @File    : serviceutil.py

from star_app.models.services import Services
from django.forms.models import model_to_dict


class ServiceUtil:

    @classmethod
    def get_service_tree_structure(cls, parent):
        """
        递归算法，生成一个树形结构
        :param parent:
        :return:
        """
        res = []
        results = Services.objects.filter(parent=parent)
        parent_name = ""
        if parent != 0:
            obj = Services.objects.filter(id=parent).first()
            parent_name = obj.name

        for i in results:
            ser = model_to_dict(i)
            ser['children'] = ServiceUtil.get_service_tree_structure(i.id)
            ser['parent_name'] = parent_name
            res.append(ser)
        return res
