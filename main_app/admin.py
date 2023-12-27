from django.contrib import admin
from .models import Snippet, Vote

admin.site.register(Snippet)
admin.site.register(Vote)

