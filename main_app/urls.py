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
]