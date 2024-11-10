from django.urls import path
from servers.views import *
urlpatterns = [
     path('genename/', IssueView.as_view(),name='genename_name'),#问答
    
]