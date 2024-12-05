from django.contrib import admin
from django.urls import path, include
from blog.views import (BaseView, 
                        PostDetailView, 
                        CreatePost, 
                        UpdatePostView, 
                        DeletePostView, 
                        GalleryView, 
                        AboutMeView,
                        CreateAboutMeView,
                        UpdateAboutMeView,
                        CreateCategoryView)
                        #SearchPostView    
from . import views

urlpatterns = [
    path('', BaseView.as_view(),name='home'),
    path('post_detail/<int:pk>', PostDetailView.as_view(),name='post_detail'),
    path('add_post/', CreatePost.as_view(),name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(),name='update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(),name='delete_post'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('post_list/', views.search_post, name='post_search'),
    path('about_me/',AboutMeView.as_view(), name='about_me'),
    path('update_about_me/<int:pk>', UpdateAboutMeView.as_view(),name='update_about_me'),
    path('create_about_me/', CreateAboutMeView.as_view(),name='create_about_me'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category')
    #path('delete-image/<int:pk>/', views.delete_image, name='delete_image'),
    
]