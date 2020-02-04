from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Josh H.',
        'title': 'Blog Post 1',
        'content': 'First Post!',
        'date_posted': '1/22/2020'
    },
    {
        'author': 'Josh H.',
        'title': 'Blog Post 2',
        'content': 'Second Post!',
        'date_posted': '1/22/2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


