from django.urls import path, include
from .views import Logout

urlpatterns = [
    path('', Logout.as_view(), name='logout'),
]