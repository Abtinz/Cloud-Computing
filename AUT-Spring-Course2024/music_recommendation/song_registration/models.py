from django.db import models

"""
    this data class will save users requests for songs in database
    id is primary key for each request
    user email will be used for shezam api results, if api find the related songs, this email will receive a message of them
    song_id is an id for song ,will find from shezam api
"""
class SongRequests(models.Model):

    id=models.AutoField(primary_key=True)
    email = models.EmailField()
    status = models.CharField(choices=['pending', 'failure', 'ready','done'], default='pending')
    song_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.song_id + "//" + self.email

    