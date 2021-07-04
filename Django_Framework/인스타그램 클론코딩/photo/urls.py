from django.urls import path
from .views import PhotoList, PhotoDelete, PhotoDetail, PhotoUpdate, PhotoCreate, \
    PhotoLike, PhotoSaved, PhotoLikeList, PhotoSavedList, PhotoMyList

# app_name 설정 : 다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해 사용
app_name = "photo"

urlpatterns = [
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>/",PhotoDelete.as_view(),name='delete'),
    path("update/<int:pk>/",PhotoUpdate.as_view(),name='update'),
    path("detail/<int:pk>/",PhotoDetail.as_view(),name='detail'),
    path("",PhotoList.as_view(),name='index'),
    path("like/<int:photo_id>",PhotoLike.as_view(),name='like'),
    path("saved/<int:photo_id>",PhotoSaved.as_view(),name='saved'),
    path("like/",PhotoLikeList.as_view(),name='like_list'),
    path("saved/",PhotoSavedList.as_view(),name='saved_list'),
    path("mylist/",PhotoMyList.as_view(),name='mylist')
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)