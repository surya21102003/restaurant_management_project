from django.shortcuts import render
from rest_framework.generics import ListAPIview
from .models imoprt MenuCategory
from .serializers import MenuCategoryserializer


class MenuCategoryListView(ListAPIview):
    querset=MenuCategory.objects.all()
    serializers_class=MenuCategoryserializer

# Create your views here.
