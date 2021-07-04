from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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
    fields = ['text','image']
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self,form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'from':form})


class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text','image']
    template_name_suffix = '_update'
    # success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request,'수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoUpdate,self).dispatch(request,*args,**kwargs)


class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request,'삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoDelete,self).dispatch(request,*args,**kwargs)


class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'

from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

class PhotoLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated: # 로그인 확인
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user

                # 클릭할 때마다 좋아요 누르기 or 좋아요 없애기
                if user in photo.like.all():
                    photo.like.remove(user)
                else:
                    photo.like.add(user)

            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class PhotoLikeList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated: # 로그인 확인
            messages.warning(request, '로그인부터 해야합니다.')
            return HttpResponseRedirect('/')
        return super(PhotoLikeList,self).dispatch(request,*args,**kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글들을 보여주기
        user = self.request.user
        queryset = user.like_post.all()
        return queryset


class PhotoSaved(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인 확인
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user

                # 클릭할 때마다 좋아요 누르기 or 좋아요 없애기
                if user in photo.saved.all():
                    photo.saved.remove(user)
                else:
                    photo.saved.add(user)
            return HttpResponseRedirect('/')


class PhotoSavedList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated: # 로그인확인
            messages.warning(request,'로그인부터 해야합니다.')
            return HttpResponseRedirect('/')
        return super(PhotoSavedList,self).dispatch(request,*args,**kwargs)

    def get_queryset(self):
        # 내가 저장한한 글들을 보여주기
        user = self.request.user
        queryset = user.saved_post.all()
        return queryset


class PhotoMyList(ListView):
    model = Photo
    template_name = 'photo/photo_mylist.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated: # 로그인 확인
            messages.warning(request,'로그인부터 해야합니다.')
            return HttpResponseRedirect('/')
        return super(PhotoMyList,self).dispatch(request,*args,**kwargs)



from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':
        # 입력 받은 내용을 이용해서 회원 객체 생성
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        return render(request, 'acceounts/signup_complete.html')
    else:
        # from 객체를 만들어서 전달
        context_values = {'form':'this is form'}
        return render(request, 'accounts/signup.html',context_values)


