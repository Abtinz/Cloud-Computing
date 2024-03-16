from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import SongRequests
from .serializers import SongRequestsSerializer,AddSongRequestsSerializer
from music_recommendation.S3_helper import upload_to_server ,create_song_url
import requests



class MusicUploadView(generics.CreateAPIView):
    
    def post(self,request):
        
        return Response({"error": "email or file is empty"}, status=400)