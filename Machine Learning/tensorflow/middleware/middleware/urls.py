from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers

from dataset import views as datasetViews

router = routers.DefaultRouter()
router.register(r'datasets', datasetViews.DatasetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls'))
]
