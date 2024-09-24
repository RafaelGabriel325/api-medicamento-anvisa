from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API Medicamento Anvisa",
        default_version='v1',
        description="API para Gerenciamento de Medicamentos da Anvisa.",
        contact=openapi.Contact(email="rafael_gabriel623@hotmail.com"),
        license=openapi.License(name="Rafael Gabriel"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('api_medicamento_anvisa.apps.api.medicamento.urls')),
]
