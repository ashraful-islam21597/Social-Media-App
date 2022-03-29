
from django.contrib import admin

from posts.models import Post, Post_reaction, Reaction, Comment, Reply

admin.site.register(Post)
admin.site.register(Post_reaction)
admin.site.register(Reaction)
admin.site.register(Comment)
admin.site.register(Reply)
