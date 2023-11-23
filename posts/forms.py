from django.forms import ModelForm
from .models import Posts, Comentarios


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'text',
        ]
        labels = {
            'title': 'Título do seu post',
            'text': 'Texto do seu post',
        }

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Texto',
        }
