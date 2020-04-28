from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from .models import Race
from .serializer import RaceSerializer
from rest_framework import generics


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class RaceList(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', RaceList)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['country_id', 'name', 'popularity', 'num_stages'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', readOnly=True,
                                                               description='Country ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Race name'),
                                          'popularity': openapi.Schema(type=openapi.TYPE_INTEGER, title='Popularity'),

                                          'num_stages': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                       title='Num of stages'),
                                      },
                                      example={
                                          'country': 1,
                                          'name': "Example name",
                                          'popularity': 1,
                                          'num_stages': 1,
                                      }
                                      )


class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    pagination_class = MyPagination
