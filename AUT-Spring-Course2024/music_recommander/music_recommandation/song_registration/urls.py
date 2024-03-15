from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registration/", include("song_registration.urls")),
    path("recommender/", include("recommender_system.urls")),
    path("shezam/", include("shezam_service.urls"))
]
