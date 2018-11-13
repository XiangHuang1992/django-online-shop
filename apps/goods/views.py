# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
# from rest_framework import generics
# from django.http import Http404

# from .models import Goods
from .serializers import GoodsSerializer

from .models import Goods
from .pagination import GoodListPagination
# Create your views here.


class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodListPagination

    def get_queryset(self):
        queryset = Goods.objects.all()
        price_min = self.request.query_params.get("price_min", 0)
        if price_min:
            queryset = queryset.filter(shop_price__gt=int(price_min))
        return queryset
