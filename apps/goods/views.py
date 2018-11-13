# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics
# from django.http import Http404

# from .models import Goods
from .serializers import GoodsSerializer

from .models import Goods
from .pagination import GoodListPagination
from .filters import GoodsFilter
# Create your views here.


class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_class = GoodsFilter
    search_fields = ('name', 'shop_price')
