from django.http import HttpResponse
from .temp_data import post_data
from django.shortcuts import render


def list_posts(request):
    context = {"posts_list": post_data}  ## Dicionário com a lista de posts
    return render(request, 'posts/index.html', context)


def detail_post(request, post_id):
    context = {'post': post_data[post_id - 1]}
    return render(request, 'posts/detail.html', context)
