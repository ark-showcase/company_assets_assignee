from django.urls import path, include
from .views import Signup

urlpatterns = [
    path('', Signup.as_view(), name='signup'),
]