from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Dashboard")

def about(request):
    judul = "<h1>About</h1>"
    subjudul = "<p> My Name is Razak</P>"
    output = judul+subjudul
    return HttpResponse(output)