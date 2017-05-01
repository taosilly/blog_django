from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post,Category

#def index(request):
#    return HttpResponse("欢迎访问我的博客首页！")

def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={
        'post_list':post_list
    })


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html',context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})