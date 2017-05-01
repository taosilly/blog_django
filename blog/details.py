from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views = int(post.views + 1)
    post.save()
    next_post = Post.objects.filter(id__gt=post.pk).first()
    previous_post = Post.objects.filter(id__lt=post.pk).order_by('-id').first()

    md = markdown.Markdown(extensions=['markdown.extensions.toc',
                                       'markdown.extensions.codehilite',
                                       TocExtension(slugify=slugify),
                                       ])
    post.body = md.convert(post.body)

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'toc': md.toc,
               'next_post': next_post,
               'previous_post': previous_post,
               }

    return render(request, 'blog/detail.html', context=context)
