from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    print(request.headers)
    return render(request, "Portfolio/index.html", {}) # response to the request
