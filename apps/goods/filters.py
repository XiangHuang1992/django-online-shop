# -*- encoding: utf-8 -*-
"""
@version: 0.1
@author: ferdinand
@email: ferinandhx@gmail.com
@flie: filters.py
@ide: PyCharm
@time: 2018/11/13 13:35
"""
from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品过滤类
    """
    min_price = filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    name = filters.CharFilter(field_name='name')

    class Meta:
        model = Goods
        fields = ['category', 'min_price', 'max_price', 'name']
