from django.shortcuts import render, redirect
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post

def index(request):
    # 블로그 메인 페이지
    post_list = Post.objects.all()  # 메인 자료 가져오기
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # 글 쓰기 등록
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)   # 폼에 입력된 자료 가져오기
        if form.is_valid():
            post = form.save(commit=False) # 가저장
            post.pub_date = timezone.now()
            post.save()     # 실제저장
            return redirect('blog:index')   # 등록 후 블로그홈으로 경로 이동
    else:
        form = PostForm()   # 비어있는 폼
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)


def introduce(request):
    # 박정재 자기소개
    return render(request, 'blog/introduce.html')

def introduce2(request):
    # 김홍연 자기소개
    return render(request, 'blog/introduce2.html')

def introduce3(request):
    # 김진희 자기소개
    return render(request, 'blog/introduce3.html')

def introduce4(request):
    # 백송희 자기소개
    return render(request, 'blog/introduce4.html')







