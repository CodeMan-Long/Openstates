from django.urls import path
from . import views

urlpatterns = [
    path("", views.overview),
    path("legislator-csv/", views.legislator_csv),
    path("geo/", views.geo),
    path("session-csv/", views.bulk_session_list, {"data_type": "csv"}),
    path("session-json/", views.bulk_session_list, {"data_type": "json"}),
]
