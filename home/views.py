from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .modelsimport MenuItem
from .serializers import MenuItemSerializer

class MenuItemPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='page_size'
    max_page_size=100

class MenuItemViewSet(viewsets.viewset):
    pagination_class=MenuItemPagination
    del list(self,request):
        query=request.query_params.get('search',None)
        items=MenuItem.objects.all()
        if query:
            items=items.filter(name__icontains=query)
            paginator=self.pagination_class()
            page=paginator.paginate_queryset(items,request)
            serializer=MenuItemSerializer(page,many=True)
            paginator.get_paginated_response(serializer.data)    

