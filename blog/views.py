from django.shortcuts import render

from .models import Post

def frontpage(request):
    posts =Post.objects.all()

    return render(request,'frontpage/frontpage.html',{'posts': posts})


def post_detail(request, slug):
    post= Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html' , {'post' : post})   

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
