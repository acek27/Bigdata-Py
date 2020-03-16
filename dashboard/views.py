from django.shortcuts import render
from .models import Post
from .forms import DataForm


def index(request):
    posts = Post.objects.filter(alamat='Situbondo')
    data = DataForm()
    context = {
        'judul': 'Dashboard',
        'header': 'Selamat Datang di Dashboard BIGDATA Kabupaten Situbondo',
        'Post': posts,
        'data':data,
    }
    return render(request, 'dashboard.html', context)
