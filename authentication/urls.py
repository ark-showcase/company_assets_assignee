from django.urls import path, include
from .components import urls as module_urls

urlpatterns = [
    path('module/', include(module_urls)),
]