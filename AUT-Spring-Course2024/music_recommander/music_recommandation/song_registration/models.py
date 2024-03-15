from django.db import models

# user song requests model
class Request(models.Model):
    
    #id will build and  increment as a primary key
    id=models.AutoField(primary_key=True)

    #this is our users email field for mail service section
    email = models.EmailField()

    #this status class will save status of request
    class Status(models.TextChoices):
            done = "done"  
            failure = "failure"
            pending = "pending"
            ready = "ready"

    status=models.CharField(max_length=50,choices=Status.choices,default=Status.pending)

    song_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description