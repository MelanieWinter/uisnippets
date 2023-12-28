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
    id_list = snippet.tags.all().values_list('id')
    tags_not_in_snippet = Tag.objects.exclude(id__in=id_list)
    print(tags_not_in_snippet)
    return render(request, 'snippets/detail.html', {
        'snippet': snippet,
        'upvote_count': upvote_count,
        'downvote_count': downvote_count,
        'vote_form' : vote_form,
        'tags': tags_not_in_snippet
    })

class SnippetCreate(CreateView):
    model = Snippet
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_not_in_snippet'] = Tag.objects.all()
        context['tags'] = 'Tags'
        return context

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'snippet_id': self.object.id})

class SnippetUpdate(UpdateView):
    model = Snippet
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_list = self.object.tags.all().values_list('id', flat=True)
        context['tags_not_in_snippet'] = Tag.objects.exclude(id__in=id_list)
        context['tags'] = 'Tags'
        return context

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'snippet_id': self.object.id})


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