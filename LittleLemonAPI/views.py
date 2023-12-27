from rest_framework import generics
from .models import menuItem
from .serializers import menuItemSerializer

# Create your views here.

class menuItemsView(generics.ListCreateAPIView):
    queryset = menuItem.objects.all()
    serializer_class = menuItemSerializer