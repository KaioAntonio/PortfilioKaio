from django.shortcuts import render

# Create your views here.
def port_page(request):
    return render(request, 'index.html')