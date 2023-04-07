from django.urls import path 
from  . import views

urlpatterns = [
    path('',views.generate_subtitles,name='generate_subtitles'),
]
