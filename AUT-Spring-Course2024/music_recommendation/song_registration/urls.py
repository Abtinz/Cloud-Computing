from django.urls import path 
from .views import MusicRequestView
urlpatterns = [

    path("song/", MusicRequestView.as_view(), name='song'),
]