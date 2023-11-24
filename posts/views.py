from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Posts, Comentarios, Categoria
from .forms import PostsForm, ComentarioForm
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

def create_comentario(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario_author = form.cleaned_data['author']
            comentario_text = form.cleaned_data['text']
            comentario = Comentarios(author=comentario_author,
                                     text=comentario_text,
                                     post=post)
            comentario.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = ComentarioForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comentario.html', context)

class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = 'posts/categorias.html'

class CategoriaCreateView(generic.CreateView):
    model = Categoria
    template_name = 'posts/create_categoria.html'
    fields = ['name', 'description', 'posts']
    success_url = reverse_lazy('posts:categorias')

class CategoriaDetailView(generic.DetailView):
    model = Categoria
    template_name = 'posts/categoria-detail.html'
