from django.contrib import admin

from .models import Post, PostImage, PostCategory, AboutMe

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    pass

class PostImageInLine(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine]
    prepopulated_fields = {'slug': ('title',)}