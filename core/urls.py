from django.contrib import admin
from django.urls import include, path

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework.routers import DefaultRouter
from .views import ParamViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'params', ParamViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_adminlte.urls')),
    path('api/', include(router.urls)),
    # Получение схемы в формате JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Интерактивный UI Swagger
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
