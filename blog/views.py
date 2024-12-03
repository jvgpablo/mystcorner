from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import  reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostImage
from .forms import PostForm, PostImageForm, EditPostForm, PostImageFormset

#Class based views

class BaseView(ListView):
    model = Post
    template_name = 'rework/post_list.html'
    
class PostDetailView(DetailView):
    model= Post
    template_name = 'rework/post_detail.html'



class AddPostInline():
    model = Post
    form_class = PostForm
    template_name = 'rework/add_post.html'

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all(x.is_valid() for x in named_formsets.values()):
            return self.render_to_response(self.get_context_data(form=form))
        
        self.object = form.save()

        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('home')
    
    def formset_images_valid(self, formset):
        images = formset.save(commit=False) 
        for image in images:
            image.post = self.object
            image.save()

class CreatePost(AddPostInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(CreatePost
    , self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                #'variants': VariantFormSet(prefix='variants'),
                'images': PostImageFormset(prefix='images'),
            }
        else:
            return {
                #'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images': PostImageFormset(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'rework/update_post.html'
    

class DeletePostView(DeleteView):
    model= Post
    template_name = 'rework/delete_post.html'
    success_url = reverse_lazy('home')


#Eliminar IMAGENES DESDE EL FORM
def delete_image(request, pk):
    try:
        image = PostImage.objects.get(id=pk)
    except PostImage.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('products:update_product', pk=image.product.id)

    image.delete()
    messages.success(
            request, 'Image deleted successfully'
            )
    return redirect('products:update_product', pk=image.product.id)

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


