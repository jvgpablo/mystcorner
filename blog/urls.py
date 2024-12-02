from django.contrib import admin
from django.urls import path, include
from blog.views import BaseView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', BaseView.as_view(),name='home'),
    path('post_detail/<int:pk>', PostDetailView.as_view(),name='post_detail'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(),name='update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(),name='delete_post'),
]