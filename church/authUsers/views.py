from django.shortcuts import render, HttpResponse

# Create your views here.
def login_user(request):
    return render(request,"login_page.html")
