from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all()
    }    
    return render(request, 'index.html', context)


def post(request, id):
    context = {
        'post': Post.objects.get(id=id)
    }
    return render(request, 'post.html', context)
