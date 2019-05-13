from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Blog
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import NewBlogForm, UpdateBlogForm, DeleteBlogForm


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


# @csrf_exempt
def delete_blog(req):
    if req.method == 'POST':
        delete_form = DeleteBlogForm(req.POST)
        if delete_form.is_valid():
            # print('id: ', delete_form.data.get('id'))
            id = delete_form.data.get('id')
            blog = get_object_or_404(Blog, id=id)
            blog.delete()

            return redirect('/')

    return redirect('/')


def update_blog(req, id):
    if req.method == 'POST':
        posted_form = UpdateBlogForm(req.POST)
        if posted_form.is_valid():
            # ###
            #
            # update
            return redirect('/')

    new_form = UpdateBlogForm()
    # get form data and pass onto render for it to be polupated
    return render(req, 'blogs/updateBlog.html', {'form': new_form, 'id': id})
