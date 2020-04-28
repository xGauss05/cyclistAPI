from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from .models import TeamRace
from .serializer import TeamRaceSerializer
from rest_framework import generics


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class TeamRaceList(generics.ListCreateAPIView):
    queryset = TeamRace.objects.all()
    serializer_class = TeamRaceSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', TeamRaceSerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['team_id', 'race_id'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', readOnly=True,
                                                               description='TeamRace ID'),
                                          'team': openapi.Schema(type=openapi.TYPE_INTEGER, title='Team ID'),
                                          'race': openapi.Schema(type=openapi.TYPE_INTEGER, title='Race ID')
                                      },
                                      example={
                                          'team': 1,
                                          'race': 1
                                      }
                                      )


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamRace.objects.all()
    serializer_class = TeamRaceSerializer
    pagination_class = MyPagination
