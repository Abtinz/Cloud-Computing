from django.urls import path 
from .views import MusicRequestView , RegisterApiMainView

urlpatterns = [

    path("song/", MusicRequestView.as_view(), name='song'),
    path("",RegisterApiMainView.as_view(), name='register'),
]