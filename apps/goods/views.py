# from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from .filters import GoodsFilter
from .models import Goods, GoodsCategory
from .pagination import GoodListPagination
# from .models import Goods
from .serializers import CategorySerializer, GoodsSerializer

# from rest_framework import generics
# from django.http import Http404

    
# Create your views here.


class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页， 分类，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = GoodListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('=name', 'goods_brief', 'goods_desc')
    ordering_fields = ('add_time', 'sold_num')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

