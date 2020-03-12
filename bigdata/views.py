from django.shortcuts import render

def index(request):
    context = {
        'judul': 'Index',
        'header': 'Selamat Datang di Index BIGDATA Kabupaten Situbondo',
        'nav' : [
            ['/','Home'],
            ['/dashboard','Dashboard'],
            ['/about','About']
        ]
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')