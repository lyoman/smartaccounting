from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class OrganogramLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class OrganogramPageNumberPagination(PageNumberPagination):
    page_size = 10