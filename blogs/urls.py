from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns=[
    path('',PostListView.as_view(),name="index"),
    path('user/<str:username>',UserPostListView.as_view(),name="user_posts"),
    path('about',views.about,name="about"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post_detail"),
    path('post/new',PostCreateView.as_view(),name="post_create"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post_update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post_delete"),
    path('author',views.search_view,name="search"),
    
]