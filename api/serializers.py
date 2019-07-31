from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name',]

class ListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
        view_name = "item-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
	added_by=UserSerializer()
	favorite_count=serializers.SerializerMethodField()
	class Meta:
		model= Item
		fields= ['name', 'image', 'description', 'detail','added_by','favorite_count',]

	def get_favorite_count(self,obj):
		return obj.what.count()
	
class FavoriteItemSerializer(serializers.ModelSerializer):
	class Meta:
		model= FavoriteItem
		fields=['user']



class DetailSerializer(serializers.ModelSerializer):
	what= FavoriteItemSerializer(many=True)
	class Meta:
		model=Item
		fields=['name', 'image', 'description','added_by','what',]



