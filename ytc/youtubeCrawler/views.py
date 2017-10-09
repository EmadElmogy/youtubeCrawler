# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pytube import YouTube
from .models import Source, Video
from .serializers import SourceSerializer, VideoSerializer



from django.shortcuts import render


# Create your views here.

def home(request):
    yt = YouTube("https://www.youtube.com/user/AsapSCIENCE/videos")
    videos = yt.get_videos()
    return render(request, 'home.html', {'videos': videos})
