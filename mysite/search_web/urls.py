from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    path('search/', views.search, name='search'),
    re_path(r'^(?P<question_id>[0-9]+)/results$', views.search, name="answer")
]