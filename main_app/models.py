from django.db import models
from django.urls import reverse

class Snippet(models.Model):
    title = models.CharField(max_length=100, default='untitled')
    description = models.CharField(max_length=500)
    html_code = models.TextField(default='<!-- html -->')
    css_code = models.TextField(default='/* css */')
    js_code = models.TextField(default='// js')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'snippet_id': self.id})