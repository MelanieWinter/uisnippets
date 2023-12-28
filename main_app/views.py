from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Snippet, Tag
from .forms import VoteForm

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
    upvote_count = snippet.vote_set.filter(vote_type='UP').count()
    downvote_count = snippet.vote_set.filter(vote_type='DOWN').count()
    vote_form = VoteForm()
    return render(request, 'snippets/detail.html', {
        'snippet': snippet,
        'upvote_count': upvote_count,
        'downvote_count': downvote_count,
        'vote_form' : vote_form
    })

class SnippetCreate(CreateView):
    model = Snippet
    fields = '__all__'

class SnippetUpdate(UpdateView):
    model = Snippet
    fields = '__all__'

class SnippetDelete(DeleteView):
    model = Snippet
    success_url = '/snippets'

def add_vote(request, snippet_id):
    form = VoteForm(request.POST)
    if form.is_valid():
        new_vote = form.save(commit=False)
        new_vote.snippet_id = snippet_id
        new_vote.save()
    return redirect('detail', snippet_id=snippet_id)


# tag model
class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
    model = Tag

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'

class TagUpdate(UpdateView):
    model = Tag
    fields = '__all__'   

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags'

def assoc_tag(request, snippet_id, tag_id):
    Snippet.objects.get(id=snippet_id).tags.add(tag_id)
    return redirect('detail', snippet_id=snippet_id)

def remove_tag(request, snippet_id, tag_id):
    Snippet.objects.get(id=snippet_id).tags.remove(tag_id)
    return redirect('detail', snippet_id=snippet_id)