from django.shortcuts import render, redirect
from django.urls import  reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditPostForm

#Class based views

class BaseView(ListView):
    model = Post
    template_name = 'rework/post_list.html'
    
class PostDetailView(DetailView):
    model= Post
    template_name = 'rework/post_detail.html'

class AddPostView(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'rework/add_post.html'
    #fields =  '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'rework/update_post.html'
    form_class = EditPostForm

class DeletePostView(DeleteView):
    model= Post
    template_name = 'rework/delete_post.html'
    success_url = reverse_lazy('home')

#def frontpage(request):
#    posts =Post.objects.all()
#
#    return render(request,'frontpage/frontpage.html',{'posts': posts})

# def post_detail(request, slug, origin):
#     post= Post.objects.get(slug=slug)
#
#     return render(request, 'blog/post_detail.html' , {'post' : post})   

# def post_list(request):
#     posts =Post.objects.all()
#     origin_dir = 'blog/post.html'
#     return render(request,'blog/post_list.html',{
#         'posts': posts,
#         'dir_origin': origin_dir})

# def search_post(request):
#     if request.method == "POST":
#         searched = request.POST.get('searched')
#         posts = Post.objects.filter(title__contains= searched)
#         return render(request,
#                       'blog/post_search.html',
#                       {'searched': searched,
#                        'posts' : posts
#                        })
#     else:
#         return render(request, 'blog/post_search.html',{})
    
# gallery code
# def gallery_list(request):
#     posts=Post.objects.all()
#     return render(request,'gallery/gallery_list.html',{"posts" : posts} )


