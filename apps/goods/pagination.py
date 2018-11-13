# -*- encoding: utf-8 -*-
"""
@version: 0.1
@author: ferdinand
@email: ferinandhx@gmail.com
@flie: pagination.py
@ide: PyCharm
@time: 2018/11/13 11:28
"""
from rest_framework.pagination import PageNumberPagination


class GoodListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10000
