from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('snippets/', views.snippets_index, name='index'),
    path('snippets/<int:snippet_id>/', views.snippets_detail, name='detail'),
]