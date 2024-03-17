from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import SongRequests
from .serializers import SongRequestsSerializer,AddSongRequestsSerializer
from music_recommendation.S3_helper import upload_to_server ,create_song_url
import requests


class MusicRequestView(APIView):
    
    def post(self,request):
        
        return Response({"": ""}, status=200)

#this api vie will help user to find specific url of song request api
class RegisterApiMainView(APIView):
    
    def get(self,request):
        return Response({"warning": "song register system url: https://music-recommender-cloud.liara.run/register/song/"}, status=300)