from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Snippet, Tag
from .forms import VoteForm, TagForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    fields = ['title', 'description', 'html_code', 'css_code', 'js_code']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_not_in_snippet'] = Tag.objects.all()
        context['tags'] = 'Tags'
        context['tag_form'] = TagForm()
        return context

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'snippet_id': self.object.id})

class SnippetUpdate(UpdateView):
    model = Snippet
    fields = ['title', 'description', 'html_code', 'css_code', 'js_code']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetching upvote and downvote counts
        context['upvote_count'] = self.object.vote_set.filter(vote_type='UP').count()
        context['downvote_count'] = self.object.vote_set.filter(vote_type='DOWN').count()

        # Fetching tag-related data
        id_list = self.object.tags.all().values_list('id', flat=True)
        context['tags_not_in_snippet'] = Tag.objects.exclude(id__in=id_list)
        context['tags'] = 'Tags'
        context['tag_form'] = TagForm()

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
    snippet = get_object_or_404(Snippet, id=snippet_id)
    tag = get_object_or_404(Tag, id=tag_id)
    snippet.tags.add(tag)
    return redirect('snippets_update', pk=snippet.id)

def remove_tag(request, snippet_id, tag_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    tag = get_object_or_404(Tag, id=tag_id)
    snippet.tags.remove(tag)
    return redirect('snippets_update', pk=snippet.id)


def add_tag(request, snippet_id):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            snippet = Snippet.objects.get(id=snippet_id)
            snippet.tags.add(tag)
    return redirect('snippets_update', pk=snippet_id)

def search_view(request):
    query = request.GET.get('q', '')
    snippets = Snippet.objects.filter(
        Q(title__icontains=query) |              # Match in the title
        Q(tags__name__icontains=query) |         # Match in tags
        Q(html_code__icontains=query) |          # Match in HTML code
        Q(css_code__icontains=query) |           # Match in CSS code
        Q(js_code__icontains=query) |            # Match in JS code
        Q(description__icontains=query)         # Match in the description
    ).distinct()
    
    return render(request, 'search_bar.html', {'snippets': snippets, 'query': query})

def search_bar(request):
    return render(request, 'search_bar.html')
