from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from .models import Cyclist
from .serializer import CyclistSerializer
from rest_framework import generics


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class CyclistList(generics.ListCreateAPIView):
    queryset = Cyclist.objects.all()
    serializer_class = CyclistSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', CyclistSerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['team_id', 'country_id', 'specialty', 'lastname',
                                                'firstname', 'birthdate', 'popularity', 'leader',
                                                'size', 'weight', 'mountain', 'plain', 'downhilling',
                                                'sprint', 'resistance', 'recuperation', 'timetrial'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', readOnly=True,
                                                               description='Cyclist ID'),
                                          'team': openapi.Schema(type=openapi.TYPE_INTEGER, title='Team ID'),
                                          'country': openapi.Schema(type=openapi.TYPE_INTEGER, title='Country ID'),
                                          'specialty': openapi.Schema(type=openapi.TYPE_INTEGER, title='Specialty'),
                                          'lastname': openapi.Schema(type=openapi.TYPE_STRING, title='Last name'),
                                          'firstname': openapi.Schema(type=openapi.TYPE_STRING, title='First name'),
                                          'birthdate': openapi.Schema(type=openapi.TYPE_STRING, format='date',
                                                                      title='Birthdate'),
                                          'popularity': openapi.Schema(type=openapi.TYPE_INTEGER, title='Popularity'),
                                          'leader': openapi.Schema(type=openapi.TYPE_BOOLEAN, title='Leader'),
                                          'size': openapi.Schema(type=openapi.TYPE_NUMBER, title='Size'),
                                          'weight': openapi.Schema(type=openapi.TYPE_INTEGER, title='Weight'),
                                          'mountain': openapi.Schema(type=openapi.TYPE_INTEGER, title='Mountain'),
                                          'plain': openapi.Schema(type=openapi.TYPE_INTEGER, title='Plain'),
                                          'downhilling': openapi.Schema(type=openapi.TYPE_INTEGER, title='Downhilling'),
                                          'sprint': openapi.Schema(type=openapi.TYPE_INTEGER, title='Sprint'),
                                          'resistance': openapi.Schema(type=openapi.TYPE_INTEGER, title='Resistance'),
                                          'recuperation': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                         title='Recuperation'),
                                          'timetrial': openapi.Schema(type=openapi.TYPE_INTEGER, title='Timetrial'),
                                          },
                                      example={
                                          'team': 0,
                                          'country': 0,
                                          'specialty': 0,
                                          'lastname': "string",
                                          'firstname': "string",
                                          'birthdate': "2019-08-20",
                                          'popularity': 0,
                                          'leader': True,
                                          'size': 0,
                                          'weight': 0,
                                          'mountain': 0,
                                          'plain': 0,
                                          'downhilling': 0,
                                          'sprint': 0,
                                          'resistance': 0,
                                          'recuperation': 0,
                                          'timetrial': 0,
                                      }
                                      )


class CyclistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cyclist.objects.all()
    serializer_class = CyclistSerializer
    pagination_class = MyPagination


class CyclistByTeam(generics.ListAPIView):
    def get_queryset(self):
        queryset = Cyclist.objects.filter(team_id=self.kwargs['pk'])
        return queryset

    serializer_class = CyclistSerializer
    pagination_class = None
