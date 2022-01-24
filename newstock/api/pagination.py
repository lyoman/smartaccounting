from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class NewStockLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class NewStockPageNumberPagination(PageNumberPagination):
    page_size = 10