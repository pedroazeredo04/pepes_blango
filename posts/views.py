from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Posts
from .forms import PostsForm
from django.shortcuts import render, get_object_or_404
from django.views import generic

class PostsListView(generic.ListView):
    model = Posts
    template_name = 'posts/index.html'


class PostsDetailView(generic.DetailView):
    model = Posts
    template_name = 'posts/detail.html'

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Posts.objects.filter(title__icontains=search_term)
        context = {"post_list": post_list}
    
    return render(request, 'posts/search.html', context)

class PostsCreateView(generic.CreateView):
    model = Posts
    template_name = 'posts/create.html'
    form_class = PostsForm

    def get_success_url(self) -> str:
        return reverse('posts:detail', args=(self.object.id, ))

class PostsUpdateView(generic.UpdateView):
    model = Posts
    template_name = 'posts/update.html'
    form_class = PostsForm

    def get_success_url(self) -> str:
        return reverse('posts:detail', args=(self.object.id, ))

class PostsDeleteView(generic.DeleteView):
    model = Posts
    template_name = 'posts/delete.html'

    def get_success_url(self) -> str:
        return reverse('posts:index')
