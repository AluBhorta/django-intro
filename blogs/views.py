from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}

    return render(request, 'blogs/index.html', context=context)


def details(req, id):
    blog = Blog.objects.get(id=id)
    # check if blog is valid
    context = {'blog': blog}
    return render(req, 'blogs/details.html', context=context)
