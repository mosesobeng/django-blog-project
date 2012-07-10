from django.db import models
from django.contrib import admin

# Add more models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField()
    updated = models.DateField() 

class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=60)
    created = models.DateField()
    updated = models.DateField()
    post = models.ForeignKey(Post,related_name='post')

class PostAdmin(admin.ModelAdmin):
    list_display=('title','created','updated')
    search=('title','body')
    list_filter=('title','created')

class CommentAdmin(admin.ModelAdmin):
    list_display=('post','author','body','created','updated')
    list_filter=('author','created')

class CommentInline(admin.TabularInline):
    model=Comment


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
