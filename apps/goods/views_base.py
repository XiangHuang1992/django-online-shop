# -*- encoding: utf-8 -*-
"""
@version: 0.1
@author: ferdinand
@email: ferinandhx@gmail.com
@flie: views_base.py.py
@ide: PyCharm
@time: 2018/11/8 09:52
"""
from django.views.generic.base import View
from goods.models import Goods


class GoodsBaseView(View):
    """
    通过django的view实现商品的列表页
    """
    def get(self, request):
        goods = Goods.objects.all()[:10]
        json_list = []
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)
        from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        from django.core import serializers
        import json
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse

        return JsonResponse(json_data, safe=False)
