from django.urls import path
from servers.views import *
urlpatterns = [
     path('genename/', IssueView.as_view()),#问答
    
]