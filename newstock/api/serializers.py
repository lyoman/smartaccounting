from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from newstock.models import NewStock, SoldStock
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class NewStockCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    class Meta:
        model = NewStock
        fields = [
            'id',
            'user',
            'name',
            'description',
            'quantity',
            'amount'
        ]


newstock_detail_url = HyperlinkedIdentityField(
        view_name='newstock-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class NewStockDetailSerializer(ModelSerializer):
    url = newstock_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = NewStock
        fields = [
            'url',
            'id',
            'user',
            'name',
            'description',
            'quantity',
            'amount',
            'active',
            'updated',
            'timestamp'
        ]

class NewStockListSerializer(ModelSerializer):
    url = newstock_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='newstock-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = NewStock
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'description',
            'active',
            'amount',
            'quantity',
            'updated',
            'timestamp'
        ]


#####Process flow Charts
class SoldStockCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)

    class Meta:
        model = SoldStock
        fields = [
            'id',
            'user',
            'description',
            'quantity',
            'amount',
            'quantity_left',
            'stockname',
            'total_amount'
        ]


soldstock_detail_url = HyperlinkedIdentityField(
        view_name='newstock-api:detail_sold',
        lookup_field='id'#or primary key <pk>
    )

class SoldStockDetailSerializer(ModelSerializer):
    url = soldstock_detail_url
    user = UserDetailSerializer(read_only=True)
    stockname = NewStockDetailSerializer(read_only=True)

    class Meta:
        model = SoldStock
        fields = [
            'url',
            'id',
            'user',
            'description',
            'amount',
            'quantity_left',
            'stockname',
            'total_amount',
            'quantity',
            'updated',
            'timestamp'
        ]

class SoldStockListSerializer(ModelSerializer):
    url = soldstock_detail_url
    user    =   UserDetailSerializer(read_only=True)
    stockname = NewStockDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='newstock-api:delete_sold',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = SoldStock
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'stockname',
            'quantity',
            'quantity_left',
            'description',
            'amount',
            'total_amount',
            'updated',
            'timestamp'
        ]