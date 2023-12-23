from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Snippet


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def snippets_index(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/index.html', {
        'snippets': snippets
    })

def snippets_detail(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    return render(request, 'snippets/detail.html', {
        'snippet': snippet
    })

class SnippetCreate(CreateView):
    model = Snippet
    fields = '__all__'
    # success_url = '/snippets/{snippet_id}'