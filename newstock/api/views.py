from rest_framework.generics import ListAPIView

from new-stock.models import NewStock, SoldStock
# from .serializers import NewStockSerializer

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)

from .pagination import NewStockLimitOffSetPagination , NewStockPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    NewStockListSerializer,
    NewStockDetailSerializer, 
    NewStockCreateUpdateSerializer,

    SoldStockListSerializer,
    SoldStockDetailSerializer, 
    SoldStockCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class NewStockListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class NewStockCreateAPIView(CreateAPIView):
    queryset = NewStock.objects.all()
    serializer_class = NewStockCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class NewStockUpdateAPIView(RetrieveUpdateAPIView):
    queryset = NewStock.objects.all()
    serializer_class = NewStockCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class NewStockDeleteAPIView(DestroyAPIView):
    queryset = NewStock.objects.all()
    serializer_class = NewStockDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class NewStockDetailAPIView(RetrieveAPIView):
    queryset = NewStock.objects.all()
    serializer_class = NewStockDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class NewStockListAPIView(ListAPIView):
    serializer_class = NewStockListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = NewStockPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = NewStock.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset



#Creating an SoldStock
class SoldStockCreateAPIView(CreateAPIView):
    queryset = SoldStock.objects.all()
    serializer_class = SoldStockCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class SoldStockUpdateAPIView(RetrieveUpdateAPIView):
    queryset = SoldStock.objects.all()
    serializer_class = SoldStockCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class SoldStockDeleteAPIView(DestroyAPIView):
    queryset = SoldStock.objects.all()
    serializer_class = SoldStockDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class SoldStockDetailAPIView(RetrieveAPIView):
    queryset = SoldStock.objects.all()
    serializer_class = SoldStockDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class SoldStockListAPIView(ListAPIView):
    serializer_class = SoldStockListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = NewStockPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = SoldStock.objects.filter(active=True)
        id = self.request.query_params.get('stockname', None)
        if id is not None:
            queryset = queryset.filter(stockname=id)
            print("hey you", queryset)
        return queryset