from django import template
from django.db.models import Count
from ..models import Post, Category,Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post'))

@register.simple_tag
def get_post_total():
    return Post.objects.count()

@register.simple_tag
def get_categories_total():
    return Category.objects.count()

@register.simple_tag
def get_tags_total():
    return Tag.objects.count()