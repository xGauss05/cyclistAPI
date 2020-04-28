from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from .models import Specialty
from .serializer import SpecialtySerializer
from rest_framework import generics


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class SpecialtyList(generics.ListCreateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', SpecialtyList)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['name'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', readOnly=True,
                                                               description='Specialty ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Specialty name'),

                                      },
                                      example={
                                          'name': "Specialty example name",
                                      }
                                      )


class SpecialtyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    pagination_class = MyPagination
