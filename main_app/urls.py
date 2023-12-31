from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('snippets/', views.snippets_index, name='index'),
    path('snippets/<int:snippet_id>/', views.snippets_detail, name='detail'),
    path('snippets/create/', views.SnippetCreate.as_view(), name='snippets_create'),
    path('snippets/<int:pk>/update/', views.SnippetUpdate.as_view(), name='snippets_update'),
    path('snippets/<int:pk>/delete/', views.SnippetDelete.as_view(), name='snippets_delete'),
    path('snippets/<int:snippet_id>/add_vote/', views.add_vote, name='add_vote'),

    # tag
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),
    path('snippets/<int:snippet_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('snippets/<int:snippet_id>/remove_tag/<int:tag_id>/', views.remove_tag, name='remove_tag'),
    path('snippets/<int:snippet_id>/add_tag/', views.add_tag, name='add_tag'),
    path('search/', views.search_view, name='search_view'),
    path('search_bar/', views.search_bar, name='search_bar_view'),
]