from django import forms
from django.forms import inlineformset_factory
from .models import Post, PostImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'intro', 'body', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

PostImageFormSet = inlineformset_factory(
    Post,
    PostImage,
    fields=('image',),
    extra=5,  
    can_delete=True,
    widgets={
        'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
)


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body', 'image']