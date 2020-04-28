from django.urls import path
from cyclingDB_app.view_country import *
from cyclingDB_app.view_cyclist import *
from cyclingDB_app.view_stage import *
from cyclingDB_app.view_race import *
from cyclingDB_app.view_specialty import *

urlpatterns = [
    path('v1/cyclist/', CyclistList.as_view(), name='Cyclist List'),
    path('v1/cyclist/<int:pk>', CyclistDetail.as_view(), name='Cyclist Detail'),
    path('v1/country/', CountryList.as_view(), name='Country List'),
    path('v1/country/<int:pk>', CountryDetail.as_view(), name='Country Detail'),
    path('v1/cyclistbyteam/<int:pk>', CyclistByTeam.as_view(), name='Cyclist by team'),
    path('v1/stage/', StageList.as_view(), name='Stage List'),
    path('v1/stage/<int:pk>', StageDetail.as_view(), name='Stage Detail'),
    path('v1/race/', RaceList.as_view(), name='Race List'),
    path('v1/race/<int:pk>', RaceDetail.as_view(), name='Race Detail'),
    path('v1/specialty/', SpecialtyList.as_view(), name='Specialty List'),
    path('v1/specialty/<int:pk>', SpecialtyDetail.as_view(), name='Specialty Detail'),

]
