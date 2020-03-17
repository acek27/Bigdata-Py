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
            Post.objects.create(
                nama=data.cleaned_data.get('nama'),
                jenis_kelamin=data.cleaned_data.get('jenis_kelamin'),
                tempat_lahir=data.cleaned_data.get('tempat_lahir'),
                tanggal_lahir=data.cleaned_data.get('tanggal_lahir'),
                email=data.cleaned_data.get('email'),
                alamat=data.cleaned_data.get('alamat'),
                hp=data.cleaned_data.get('hp'),
            )
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
