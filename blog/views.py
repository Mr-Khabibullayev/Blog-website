from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class BlogLIstView(ListView):
    model = Post
    template_name = 'home.html'
    
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class Post_Create_Delete(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title','author','body']
    
    
class Blog_Update_View(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']
    
class Blog_Delete_View(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')