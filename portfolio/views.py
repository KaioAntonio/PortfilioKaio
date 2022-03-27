from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from portfolio.models import Mensagem

# Create your views here.

def port_page(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")

        mensagens_salvas = Mensagem.objects.create(nome=nome,email=email,mensagem=mensagem)

        return render(request,"index.html")
    else:
        return render(request, "index.html")

