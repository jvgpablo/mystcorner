from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='Uncategorized', blank=True, null=True)
    
    #class Meta:
    #    ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title
    
# ENCUENTRA ALGUNA FORMA DE QUE SOLO SE PUEDA AÑADIR UN OBJETO A ESTO
class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    paragraph_intro = models.TextField()
    paragraph_body = models.TextField(blank=True, null=True)
    paragraph_end = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('about_me')
    