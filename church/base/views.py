from django.shortcuts import render

# Create your views here.
def indexPage(request):
    return render(request,'homepage.html')

def about_us(request):
    return render(request, 'about.html')

def location(request):
    return render(request, 'locations.html')

def contact_us(request):
    return render(request, 'contact.html')