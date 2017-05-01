from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm
import markdown


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
                                       'markdown.extensions.toc',
                                       ])
    html = md.convert(post.body)

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'toc': md.toc,
               'html':html
               }

    return render(request, 'blog/detail.html', context=context)
