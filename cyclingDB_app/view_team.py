from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from .models import Team
from .serializer import TeamSerializer
from rest_framework import generics


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', TeamSerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['country_id', 'name', 'manager'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', readOnly=True,
                                                               description='Team ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Team Name'),
                                          'manager': openapi.Schema(type=openapi.TYPE_STRING, title='Manager name')
                                      },
                                      example={
                                          'name': "Team name example",
                                          'manager': "Manager name example"
                                      }
                                      )


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = MyPagination
