from django import forms
from .models import Post, PostImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'intro', 'body', 'author')

        widgets= {
            'title' : forms.TextInput(attrs={'class' : 'form-control' }),
            'slug' : forms.TextInput(attrs={'class' : 'form-control' }),
            'intro' : forms.Textarea(attrs={'class' : 'form-control' }),
            'body' : forms.Textarea(attrs={'class' : 'form-control' }),
            'author' : forms.Select(attrs={'class' : 'form-control' })
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'intro', 'body')

        widgets= {
            'title' : forms.TextInput(attrs={'class' : 'form-control' }),
            'slug' : forms.TextInput(attrs={'class' : 'form-control' }),
            'intro' : forms.Textarea(attrs={'class' : 'form-control' }),
            'body' : forms.Textarea(attrs={'class' : 'form-control' })
        }
