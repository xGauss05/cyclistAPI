from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from .models import Stage
from .serializer import StageSerializer
from rest_framework import generics


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class StageList(generics.ListCreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', StageList)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['race_id', 'specialty', 'name', 'day', 'month', 'stage_number',
                                                'stage_km'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', readOnly=True,
                                                               description='Stage ID'),
                                          'race': openapi.Schema(type=openapi.TYPE_INTEGER, title='Race ID'),
                                          'specialty': openapi.Schema(type=openapi.TYPE_INTEGER, title='Specialty ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Race name'),
                                          'day': openapi.Schema(type=openapi.TYPE_INTEGER, title='Day'),
                                          'month': openapi.Schema(type=openapi.TYPE_INTEGER, title='Month'),
                                          'stage_number': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                         title='Stage Number'),
                                          'stage_km': openapi.Schema(type=openapi.TYPE_INTEGER, title='Stage KM'),
                                      },
                                      example={
                                          'race': 1,
                                          'specialty': 1,
                                          'name': "Example name",
                                          'day': 1,
                                          'month': 1,
                                          'stage_number': 1,
                                          'stage_km': 1
                                      }
                                      )


class StageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    pagination_class = MyPagination
