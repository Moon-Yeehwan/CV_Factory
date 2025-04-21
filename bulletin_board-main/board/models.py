from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 날짜

    def __str__(self):
        return self.title  # 제목을 표시
