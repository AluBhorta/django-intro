from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

from .forms import NewBlogForm


def index(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}

    return render(request, 'blogs/index.html', context=context)


def details(req, id):
    blog = Blog.objects.get(id=id)
    # ### check if blog is valid
    context = {'blog': blog}
    return render(req, 'blogs/details.html', context=context)


def add_blog(req):
    if req.method == 'POST':
        posted_form = NewBlogForm(req.POST)
        if posted_form.is_valid():
            posted_form.save()
            return redirect('/')

    new_form = NewBlogForm()
    return render(req, 'blogs/addBlog.html', {'form': new_form})


def delete_blog(self, id):
    Blog.delete(id=id)
    return redirect('/')


def update_blog(self, id):
    pass
