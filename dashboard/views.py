from django.shortcuts import render
from .models import Post


def dashboard(request):
    posts = Post.objects.filter(alamat='Situbondo')
    context = {
        'judul': 'Dashboard',
        'header': 'Selamat Datang di Dashboard BIGDATA Kabupaten Situbondo',
        'Post': posts,
    }
    return render(request, 'dashboard.html', context)
