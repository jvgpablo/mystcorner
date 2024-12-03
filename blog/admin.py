from django.contrib import admin

from .models import Post, PostImage, PostCategory

class PostImageInLine(admin.TabularInline):
    model = PostImage
    extra = 1
admin.register(PostCategory)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine]
    prepopulated_fields = {'slug': ('title',)}