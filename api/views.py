from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
									RetrieveAPIView, 
									RetrieveUpdateAPIView, 
									DestroyAPIView, 
									CreateAPIView)
from items.models import Item, FavoriteItem
from .serializers import ListSerializer, DetailSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsWhat
from rest_framework.filters import SearchFilter, OrderingFilter


class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ListSerializer
	permission_classes = [IsAuthenticated]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name']

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	
	permission_classes =[IsWhat]
	

