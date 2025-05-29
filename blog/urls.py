from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.all_posts, name='all-posts'),
    path('posts/<slug:slug>/', views.post_detail, name='post-detail'),
    path('authors/', views.authors_list, name='authors-list'),
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    path('tags/', views.tag_list, name="tag-list"),
    path('tags/<int:pk>/', views.tag_post, name="tag-post"),
]
