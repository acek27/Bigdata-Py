from django.shortcuts import render

def dashboard(request):
    context = {
        'judul' : 'Dashboar',
        'header' : 'Selamat Datang di Dashboard BIGDATA Kabupaten Situbondo'
    }
    return render(request,'dashboard.html', context)