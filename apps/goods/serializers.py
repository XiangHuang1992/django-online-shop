# -*- encoding: utf-8 -*-
"""
@version: 0.1
@author: ferdinand
@email: ferinandhx@gmail.com
@flie: serializers.py.py
@ide: PyCharm
@time: 2018/11/8 12:01
"""
from rest_framework import serializers

from .models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"

    # name = serializers.CharField()
    # click_num = serializers.IntegerField()
    # sold_num = serializers.IntegerField()
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.click_num = validated_data.get('click_num', instance.click_num)
    #     instance.sold_num = validated_data.get('sold_num', instance.sold_num)
    #     instance.save()
    #     return instance
    #
    # def create(self, validated_data):
    #     return Goods.objects.create(**validated_data)
