from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostsListView.as_view(), name='index'),
    path('create/', views.PostsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PostsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostsDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.PostsDetailView.as_view(), name='detail'),
    path('search/', views.search_posts, name='search'),
    path('<int:post_id>/comentario/', views.create_comentario, name='comentario'),

]
