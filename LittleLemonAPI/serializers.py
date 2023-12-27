from rest_framework import serializers
from .models import menuItem

class menuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = menuItem
        fields = ['id', 'title', 'price', 'inventory']