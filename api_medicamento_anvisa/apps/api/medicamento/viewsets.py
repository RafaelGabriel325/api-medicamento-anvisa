from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import APIException
from api_medicamento_anvisa.apps.core.medicamento import models
from api_medicamento_anvisa.apps.api.medicamento import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MedicacaoPagination(PageNumberPagination):
    page_size = 25


class MedicacaoViewSet(viewsets.ReadOnlyModelViewSet):  # Mantenha como ReadOnlyModelViewSet
    queryset = models.Medicacao.objects.all()
    serializer_class = serializers.MedicacaoSerializer
    pagination_class = MedicacaoPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'substancia', openapi.IN_QUERY, description="Filtra por substância", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'cnpj', openapi.IN_QUERY, description="Filtra por CNPJ", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'laboratorio', openapi.IN_QUERY, description="Filtra por laboratório", type=openapi.TYPE_STRING
            ),
        ]
    )
    def list(self, request):
        try:
            queryset = self.queryset
            if request.query_params:
                queryset = self.aplicar_filtros(queryset, request.query_params)
            page = self.paginate_queryset(queryset)
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as exception:
            raise APIException(f"Erro ao listar medicamentos: {str(exception)}")


    def aplicar_filtros(self, queryset, params):
        substancia = params.get('substancia')
        cnpj = params.get('cnpj')
        laboratorio = params.get('laboratorio')

        try:
            if substancia:
                queryset = queryset.filter(substancia__icontains=substancia)
            if cnpj:
                queryset = queryset.filter(cnpj__icontains=cnpj)
            if laboratorio:
                queryset = queryset.filter(laboratorio__icontains=laboratorio)
        except Exception as exception:
            raise APIException(f"Erro ao aplicar filtros: {str(exception)}")

        return queryset
