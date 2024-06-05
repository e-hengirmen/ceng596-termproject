
from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    # path('/', include('search.urls')),
    path(
        '',
        SearchPageView.as_view(),
        name=SearchPageView.url_name
    ),
    re_path(
        r'results/(?P<query>\w+)',
        ResultPageView.as_view(),
        name=ResultPageView.url_name
    ),
    re_path(
        r'doc/(?P<document_id>\d+)>',
        DocumentPageView.as_view(),
        name=DocumentPageView.url_name
    ),
]
