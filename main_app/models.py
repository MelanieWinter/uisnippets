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
    
class Vote(models.Model):
    VOTE_CHOICES = [
        ('UP', 'Upvote'),
        ('DOWN', 'Downvote'),
    ]

    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=4, choices=VOTE_CHOICES, default='UP')

    def __str__(self):
        return f'{self.get_vote_type_display()} for {self.snippet.title}'