from django.db import models

class Snippet(models.Model):
    CODE_TYPE_CHOICES = [
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('js', 'JavaScript'),
        ('python', 'Python'),
        ('java', 'Java'),
    ]

    title = models.CharField(max_length=100)
    primary_code_type = models.CharField(max_length=10, choices=CODE_TYPE_CHOICES)
    description = models.TextField(default=' ')
    code = models.TextField(default=' ')

    def __str__(self):
        return self.title