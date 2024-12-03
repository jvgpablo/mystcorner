from django.shortcuts import render, redirect
from django.urls import  reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Post  
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from .forms import PostForm, EditPostForm, PostForm, PostImageFormSet

def frontpage(request):
    posts =Post.objects.all()

    return render(request,'frontpage/frontpage.html',{'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    images = post.images.all()  
    return render(request, 'rework/post_detail.html', {'post': post, 'images': images})

def post_list(request):
    posts =Post.objects.all()
    origin_dir = 'blog/post.html'
    return render(request,'blog/post_list.html',{
        'posts': posts,
        'dir_origin': origin_dir})

def search_post(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        posts = Post.objects.filter(title__contains= searched)
        return render(request,
                      'blog/post_search.html',
                      {'searched': searched,
                       'posts' : posts
                       })
    else:
        return render(request, 'blog/post_search.html',{})
    
#gallery code
def gallery_list(request):
    posts=Post.objects.all()
    return render(request,'gallery/gallery_list.html',{"posts" : posts} )


#Class based views

class BaseView(ListView):
    model = Post
    template_name = 'rework/post_list.html'
    
class PostDetailView(DetailView):
    model= Post
    template_name = 'rework/post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'rework/add_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PostImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PostImageFormSet()
        return context

    def form_valid(self, form):
        
        response = super().form_valid(form)
        
       
        formset = PostImageFormSet(self.request.POST, self.request.FILES, instance=form.instance)
        if formset.is_valid():
            formset.save() 

        return response



class UpdatePostView(UpdateView):
    model = Post
    template_name = 'rework/update_post.html'
    form_class = EditPostForm

class DeletePostView(DeleteView):
    model= Post
    template_name = 'rework/delete_post.html'
    success_url = reverse_lazy('home')