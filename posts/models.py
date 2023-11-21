from django.db import models
from django.conf import settings

class Posts(models.Model):
    title = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.title}'


class Comentarios(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
