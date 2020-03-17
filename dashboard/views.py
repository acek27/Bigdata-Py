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
    data = DataForm()
    if request.method == 'POST':
        Post.objects.create(
            nama=request.POST.get('nama'),
            jenis_kelamin=request.POST.get('jenis_kelamin'),
            tempat_lahir=request.POST.get('tempat_lahir'),
            tanggal_lahir=request.POST.get('tanggal_lahir'),
            email=request.POST.get('email'),
            alamat=request.POST.get('alamat'),
            hp=request.POST.get('hp'),
        )
        return HttpResponseRedirect("/dashboard/")

    context = {
        'judul': 'Biodata User',
        'header': 'Pengisian Form Biodata User',
        'data': data,
    }
    return render(request, 'create.html', context)

def create(request):
    data = DataForm()
    if request.method == 'POST':
        Post.objects.create(
            nama=request.POST.get('nama'),
            jenis_kelamin=request.POST.get('jenis_kelamin'),
            tempat_lahir=request.POST.get('tempat_lahir'),
            tanggal_lahir=request.POST.get('tanggal_lahir'),
            email=request.POST.get('email'),
            alamat=request.POST.get('alamat'),
            hp=request.POST.get('hp'),
        )
        return HttpResponseRedirect("/dashboard/")

    context = {
        'judul': 'Biodata User',
        'header': 'Pengisian Form Biodata User',
        'data': data,
    }
    return render(request, 'create.html', context)
