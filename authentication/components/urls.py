from django.urls import path, include
from .signup import urls as signup_urls
from .login import urls as login_urls
from .logout import urls as logout_urls

urlpatterns = [
    path('signup/', include(signup_urls)),
    path('login/', include(login_urls)),
    path('logout/', include(logout_urls)),
]