import operator
import requests
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UserCreateForm
from .filters import PostFilter


def register(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created Successfully")
            return redirect('login')
    context={'form':form}
    return render(request, 'accounts/register.html', context)

def cuslogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "LoggedIn successful")
        else:
            messages.error(request, "Incorrect Credentials")

        return redirect('index')

    return render(request, 'accounts/login.html')

class HomeView(ListView):
    model = Post
    template_name = 'blogapp/index.html'
    ordering = ['-modified_at']

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context



class ArticleDetail(DetailView):
    model = Post
    template_name = 'blogapp/articles.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogapp/addpost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    template_name = 'blogapp/updatepost.html'
    form_class = PostForm


class DeletePost(DeleteView):
    model = Post
    template_name = 'blogapp/deletepost.html'
    success_url = reverse_lazy('index')


def logout_view(request):
    logout(request)
    return redirect('index')

