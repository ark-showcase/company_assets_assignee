from django.urls import path, include
from .assign_employee_asset import urls as assign_employee_asset_urls
from .assign_employee import urls as assign_employee_urls
from .assign_asset import urls as assign_asset_urls
from .view_asset import urls as view_asset_urls

urlpatterns = [
    path('assign_employee_asset/', include(assign_employee_asset_urls)),
    path('assign_employee/', include(assign_employee_urls)),
    path('assign_asset/', include(assign_asset_urls)),
    path('view_asset/', include(view_asset_urls)),
]