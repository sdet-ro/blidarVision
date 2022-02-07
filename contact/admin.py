from django.contrib import admin
from .models import Post, Application, Message, FloaterMessage
# Register your models here.
admin.site.register(Message)
admin.site.register(FloaterMessage)
admin.site.register(Application)


class PostAdmin(admin.ModelAdmin):
    # list_display = ('title', 'slug', 'status', 'created_on', 'blog_images')
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fileds = ['title', 'content']

admin.site.register(Post, PostAdmin)    

