from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog
from .forms import NewBlogForm, UpdateBlogForm, DeleteBlogForm


def index(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context=context)


def details(req, id):
    blog = get_object_or_404(Blog, id=id)
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


def delete_blog(req):
    if req.method == 'POST':
        delete_form = DeleteBlogForm(req.POST)
        if delete_form.is_valid():
            id = delete_form.data.get('id')
            blog = get_object_or_404(Blog, id=id)
            blog.delete()
            return redirect('/')


def update_blog(req, id):
    if req.method == 'POST':
        update_form = UpdateBlogForm(req.POST)
        if update_form.is_valid():
            newBlog = update_form.cleaned_data
            oldBlog = Blog.objects.get(id=id)

            setattr(oldBlog, 'title', newBlog['title'])
            setattr(oldBlog, 'author', newBlog['author'])
            setattr(oldBlog, 'body', newBlog['body'])
            oldBlog.save()

        return redirect('/')

    updateBlog = Blog.objects.get(id=id)
    context = {'blog': updateBlog}
    return render(req, 'blogs/updateBlog.html', context=context)
