from django.urls import path, include
from .views import ViewAssets

urlpatterns = [
    path('', ViewAssets.as_view(), name='view_asset'),
]