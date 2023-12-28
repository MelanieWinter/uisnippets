from django.forms import ModelForm
from .models import Vote, Tag

class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['vote_type']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'