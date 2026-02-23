from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/',include('management.urls')),
    path('project/',include('auth_management.urls'))
]
