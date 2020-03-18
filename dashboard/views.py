from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import DataForm


def index(request):
    posts = Post.objects.all()
    context = {
        'judul': 'Dashboard',
        'header': 'Selamat Datang di Dashboard BIGDATA Kabupaten Situbondo',
        'Post': posts,
    }
    return render(request, 'dashboard.html', context)


def create(request):
    data = DataForm(request.POST or None)
    error = None
    if request.method == 'POST':
        if data.is_valid():
            data.save()
            return HttpResponseRedirect("/dashboard/")
        else:
            error = data.errors

    context = {
        'judul': 'Biodata User',
        'header': 'Pengisian Form Biodata User',
        'data': data,
        'error': error
    }
    return render(request, 'create.html', context)
