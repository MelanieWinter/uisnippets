from django.contrib import admin
from .models import Snippet, Vote, Tag

admin.site.register(Snippet)
admin.site.register(Vote)
admin.site.register(Tag)

