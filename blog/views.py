from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import  os

#def index(request):
#    return HttpResponse("欢迎访问我的博客首页！")

def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', context={
        'post_list': posts
    })


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html',context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, category_pinyin):
    #cate = get_object_or_404(Category, pk=pk)
    cate = Category.objects.filter(pinyin = category_pinyin).first()
    cate.images = os.path.join('/uploads/',str(cate.images))
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/category.html', context={'post_list': post_list, 'category': cate})
