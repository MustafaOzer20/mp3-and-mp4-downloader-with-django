from django.shortcuts import render,redirect,HttpResponse
from .forms import LinkForm,DocumentForm
from django.contrib import messages
# Create your views here.
from pytube import YouTube
from bs4 import BeautifulSoup
import requests
import os
from django.core.files.storage import FileSystemStorage

def mp3(request):
    form = LinkForm(request.POST or None)

    if form.is_valid():
        try:
            os.chdir('C:/PYazilim/media') 
            ls = os.listdir('C:/PYazilim/media')
            os.remove(ls[0]) ; os.remove(ls[1])
        except:
            pass

        vid = form.save(commit=False)
        video_link=vid.vid_link
        vid = YouTube(video_link).streams.first()
        a = vid
        vid.download(output_path="C:/PYazilim/media", filename="test")

        response = requests.get(video_link)
        html_ic = response.content
        soup = BeautifulSoup(html_ic, "html.parser")
        name = soup.find_all('title')
        name = str(name[0].text)[:(len(name[0].text)-10)]

        os.chdir('C:/PYazilim/media') 
        os.rename('test.mp4','test.mp3')
        a.download(output_path="C:/PYazilim/media", filename="test")
        os.chdir('C:/PYazilim/media') 
        os.rename('test.mp4',f'{name}.mp4')
        os.rename('test.mp3',f'{name}.mp3')
        return render(request,"mp3.html",{"name":name})

    return render(request,"mp3.html",{"form":form})


