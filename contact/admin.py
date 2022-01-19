from django.contrib import admin
from .models import Application, Message, FloaterMessage, Post

# Register your models here.
admin.site.register(Message)
admin.site.register(FloaterMessage)
admin.site.register(Application)
admin.site.register(Post)