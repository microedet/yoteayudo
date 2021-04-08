from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def about_us(request):
    return render(request,"core/about_us.html")

def contact_us(request):
    return render(request,"core/contact_us.html")

def gallery(request):
    return render(request,"core/gallery.html")

def services(request):
    return render(request,"core/services.html")

def blog(request):
    return render(request,"core/blog.html")

