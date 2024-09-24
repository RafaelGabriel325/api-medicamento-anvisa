from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_medicamento_anvisa.apps.api.medicamento.viewsets import MedicacaoViewSet

router = DefaultRouter()
router.register(r'medicacoes', MedicacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
