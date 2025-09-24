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
    def update(self,request,pk=None):
        item=get_object_or_404(MenItem,pk=pk)
        serializer=MenuItemSerializer(item,data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_400_bad_request)

class MenuItemByCategoryView(APIView):
    def get(self,request):
        category_name=request.query_params.get("category",None)
        if not category_name:
            return Resposne({"error":"category query isrequired"},status=status.HTTP_400_bad_request)
            items=MenuItem.objects.filter(category__category_name__iexact=category_name)

            if not items.exists():
                return resposne({"message":f"no menu"},status=status.HTTP_404_not_found)
            serializer=MenuItemSerializer(items,many=True)
            return Response(serializer.data,status=status.HTTP_200_ok)    
