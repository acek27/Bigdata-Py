from django.shortcuts import render

def index(request):
    context = {
        'judul': 'Dashboard',
        'header': 'Selamat Datang di Index BIGDATA Kabupaten Situbondo',
        'banner': 'img/home.jpg',
        'nav' : [
            ['/','Home'],
            ['/dashboard','Dashboard'],
            ['/about','About'],
        ]
    }
    return render(request,'index.html',context)

def about(request):
    context = {
        'judul': 'About',
        'header': 'Selamat Datang di About BIGDATA Kabupaten Situbondo',
        'banner': 'img/home.jpg',
        'nav': [
            ['/', 'Home'],
            ['/dashboard', 'Dashboard'],
            ['/about', 'About'],
        ]
    }
    return render(request,'about.html', context)