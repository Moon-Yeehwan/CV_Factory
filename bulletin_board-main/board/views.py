from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신 글부터 정렬
    return render(request, 'board/post_list.html', {'posts': posts})
