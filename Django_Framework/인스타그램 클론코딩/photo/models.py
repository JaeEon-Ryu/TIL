from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# 모델 구현 - DB에 저장될 데이터들을 클래스 형태로 구현
# 데이터의 동작을 함께 정의한다 ( CRUD : 저장, 읽기, 수정, 삭제 )
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # adming 사이트 화면 표시 구현
    def __str__(self):
        return "text : " + self.text

    # ordering 정렬
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail',args=[self.id])