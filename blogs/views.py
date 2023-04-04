from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User



def index(request):
    return render(request,"blogs/index.html",{
        "posts" : Post.objects.all(),"title":"bolgs",
    })


class PostListView(ListView):
    model=Post
    template_name="blogs/index.html"
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5

class UserPostListView(ListView):
    model=Post
    template_name="blogs/user_posts.html"
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


    


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
        

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/blogs'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request,"blogs/about.html",{
        "title":"about"
    })

def search_view(request):   
    if request.method=="POST":
        searched=request.POST['searched']
        user_posts=Post.objects.filter(author__username__contains=searched)
        return render(request,'blogs/search_venue.html',{
            'searched':searched,
            'user_posts':user_posts
        })
    else:
        return render(request,'blogs/search_venue.html')