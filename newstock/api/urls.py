from django.contrib import admin
from django.urls import path

from .views import (
    NewStockListAPIView,
    NewStockDeleteAPIView,
    NewStockDetailAPIView,
    NewStockUpdateAPIView,
    NewStockCreateAPIView,

    SoldStockListAPIView,
    SoldStockDeleteAPIView,
    SoldStockDetailAPIView,
    SoldStockUpdateAPIView,
    SoldStockCreateAPIView,
    SoldStockUserListAPIView,
	)

urlpatterns = [
    path('new_stock/', NewStockListAPIView.as_view(), name='list'),
    path('new_stock/new/', NewStockCreateAPIView.as_view(), name='new'),
    path('new_stock/<int:id>/detail/', NewStockDetailAPIView.as_view(), name='detail'),
    path('new_stock/<int:id>/edit/', NewStockUpdateAPIView.as_view(), name='update'),
    path('new_stock/<int:id>/delete/', NewStockDeleteAPIView.as_view(), name="delete"),

    ##### process flow
    path('sold_stock/', SoldStockListAPIView.as_view(), name='sold_stock'),
    path('sold_stock_user/', SoldStockUserListAPIView.as_view(), name='sold_stock_user'),
    path('sold_stock/new/', SoldStockCreateAPIView.as_view(), name='new_sold'),
    path('sold_stock/<int:id>/detail/', SoldStockDetailAPIView.as_view(), name='detail_sold'),
    path('sold_stock/<int:id>/edit/', SoldStockUpdateAPIView.as_view(), name='update_sold'),
    path('sold_stock/<int:id>/delete/', SoldStockDeleteAPIView.as_view(), name="delete_sold"),

]
