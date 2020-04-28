"""cyclistAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cyclingDB_app.view_cyclist import CyclistByTeam

schema_view = get_schema_view(
    openapi.Info(
        title="Cycling API",
        default_version='v1',
        description="Road Cycling Database",
        terms_of_service="https:/www.google.com/policies/terms/",
        contact=openapi.Contact(email="jcacaynes@gmail.com"),
        license=openapi.License(name="Apache 2.0"),

    ),
    public =True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('cyclingDB_app/', include('cyclingDB_app.urls'))

]
