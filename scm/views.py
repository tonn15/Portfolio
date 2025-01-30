from django.shortcuts import render

def index (request):
    return render(request,'scm/index.html')
def about(request):
    return render(request,'scm/about.html')
def service(request):
    return render(request,'scm/service.html')
def contact(request):
    return render(request,'scm/contactus.html')
