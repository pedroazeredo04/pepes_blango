from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Posts
from django.shortcuts import render, get_object_or_404


def list_posts(request):
    post_data = Posts.objects.all()
    context = {"posts_list": post_data}  ## Dicionário com a lista de posts
    return render(request, 'posts/index.html', context)


def detail_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)


def create_post(request):
    if request.method == 'POST':
        requested_post_name = request.POST['post_title']
        requested_post_text = request.POST['post_text']
        post = Posts(title=requested_post_name,
                     text=requested_post_text)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})


def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Posts.objects.filter(title__icontains=search_term)
        context = {"post_list": post_list}
    
    return render(request, 'posts/search.html', context)


def update_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        post.title = request.POST['post_title']
        post.text = request.POST['post_text']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'posts/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)
