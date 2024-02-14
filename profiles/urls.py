from django.urls import path
from .views import UserCreateView, PostCreateView, PostListView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('create-post/', PostCreateView.as_view(), name='post-create'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
]
