from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from tbbl.views import *

urlpatterns = [
    url(r'^scripts/', ScriptView.as_view()),
    url(r'^csvs/', CsvScriptsView.as_view()),
]
