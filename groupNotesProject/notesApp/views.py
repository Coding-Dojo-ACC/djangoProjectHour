from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")
