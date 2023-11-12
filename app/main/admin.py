from django.contrib import admin
from .models import Board, Thread, Post
# Register your models here.


admin.site.register(Board)
admin.site.register(Thread)
admin.site.register(Post)