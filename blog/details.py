from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #post.body = markdown.markdown(post.body,
    #                              extensions=[
    #                                  'markdown.extensions.extra',
    #                                  'markdown.extensions.codehilite',
    #                                  'markdown.extensions.toc',
    #                              ])
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
               }

    return render(request, 'blog/detail.html', context=context)
