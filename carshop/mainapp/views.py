from django.shortcuts import render

# Create your views here.

def homeView(request):
    template = 'mainapp/home.html'
    contaxt = {}

    return render(request, template_name= template, context= contaxt)

def aboutView(request):
    template = 'mainapp/about.html'
    contaxt = {}

    return render(request, template_name= template, context= contaxt)

def contactView(request):
    template = 'mainapp/contact.html'
    contaxt = {}

    return render(request, template_name= template, context= contaxt)

