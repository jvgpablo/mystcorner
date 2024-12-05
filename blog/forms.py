from django import forms
from django.forms import inlineformset_factory, ValidationError
from .models import Post, PostImage, PostCategory, AboutMe

choice_list = []

if PostCategory.objects.exists():
    choices = PostCategory.objects.all().values_list('name', 'name')
    for item in choices:
        choice_list.append(item)
else:
    print('No categories found in PostCategory, defaulting to "uncategorized')
    choice_list.append(('uncategorized','uncategorized'))
    print('Categories list: ',choice_list)




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'intro', 'body', 'author', 'category')

        widgets= {
            'title' : forms.TextInput(attrs={'class' : 'form-control' }),
            'slug' : forms.TextInput(attrs={'class' : 'form-control' }),
            'intro' : forms.Textarea(attrs={'class' : 'form-control' }),
            'body' : forms.Textarea(attrs={'class' : 'form-control' }),
            'author' : forms.Select(attrs={'class' : 'form-control' }),
            'category' : forms.Select(choices=choice_list, attrs={'class' : 'form-control' })
        }

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = '__all__'

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

PostImageFormset = inlineformset_factory(
    parent_model = Post,
    model = PostImage,
    form = PostImageForm,
    extra = 1,
    can_delete=False
)


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'

        widgets= {
            'title' : forms.TextInput(attrs={'class' : 'form-control' }),
            'paragraph_intro' : forms.TextInput(attrs={'class' : 'form-control' }),
            'paragraph_body' : forms.Textarea(attrs={'class' : 'form-control' }),
            'paragraph_end' : forms.Textarea(attrs={'class' : 'form-control' })
        }

    def clean(self):
        if not self.instance.pk and AboutMe.objects.exists():
            raise ValidationError('Solo se puede tener un objeto "about me"')
        return super().clean()
    
class PostCategoryForm(forms.ModelForm):
    class Meta:
        model= PostCategory
        fields = '__all__'
        
        widgets = {
            'name' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'slug' : forms.TextInput(attrs = {'class' : 'form-control'})
        }