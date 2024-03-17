from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import SongRequests
from .serializers import SongRequestsSerializer,AddSongRequestsSerializer
from music_recommendation.S3_helper import upload_to_server ,create_song_url
import requests
from rest_framework import generics

class MusicRequestView(generics.CreateAPIView):
    serializer_class=AddSongRequestsSerializer
    queryset=SongRequests.objects.all()
    def post(self,request):

        #receiving the email of user from json form
        request_data={
            "email":request.data["email"]
        }

        serializer=SongRequestsSerializer(data=request_data)
        #check if the data is valid
        if(serializer.is_valid()):

            #now we need to save and upload our data to Dbas and S3 cloud services
            
            serializer.save()
            song_request=serializer.data

            #uploading the request and song to the server
            request_id =song_request['id']
            song_file=request.data['song_file']

            print(request_id)
            print(song_file)
            
            #saving the music file and request id in s3 cloud
            url = upload_to_server(music_file = song_file,song_id = request_id)

            if(url):
                return Response({"1": "1"}, status=200)
            else:
                return Response({"2": "2"}, status=200)
        else:
            pass


        return Response({"": ""}, status=200)

#this api vie will help user to find specific url of song request api
class RegisterApiMainView(APIView):
    
    def get(self,request):
        return Response({"warning": "song register system url: https://music-recommender-cloud.liara.run/register/song/"}, status=300)