from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('dataset/', include('dataset.urls')),
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls'))
]
