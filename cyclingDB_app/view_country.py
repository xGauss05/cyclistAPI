from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from .models import Country
from .serializer import CountrySerializer
from rest_framework import generics


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', CountrySerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['name'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', readOnly=True,
                                                               description='Country ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Name')
                                      },
                                      example={
                                          'name': "example",
                                      }
                                      )


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = MyPagination
