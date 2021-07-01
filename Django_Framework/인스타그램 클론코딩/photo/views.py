from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo

# 가장 메인에서 보여줄 로직
class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'

# 성공하면 메인 페이지로 돌아가도록 연결
class PhotoCreate(CreateView):
    model = Photo
    fields = ['test','image']
    template_name_suffix = '_create'
    success_url = '/'

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text','image']
    template_name_suffix = '_update'
    success_url = '/'

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'
