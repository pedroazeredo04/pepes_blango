from django.forms import ModelForm
from .models import Posts


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
