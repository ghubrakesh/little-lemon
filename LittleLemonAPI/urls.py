from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menuItemsView.as_view(), name='menuItems'),
]