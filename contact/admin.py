from django.contrib import admin
from .models import Post
from contact.models import Application, Message, FloaterMessage
# Register your models here.
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(FloaterMessage)
admin.site.register(Application)
