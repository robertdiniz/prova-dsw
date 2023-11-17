from django.shortcuts import render, redirect
from .models import Hospedagem
from .forms import HospedagemForm

def hospedagem(request):

    hospedagens = Hospedagem.objects.all()

    return render(request, "hospedagem/hospedagens.html", {'hospedagens': hospedagens})

def hospedagem_criar(request):

    
    if request.method == "POST":

        form = HospedagemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('hospedagem_listar')

    else:
        form = HospedagemForm()

        return render(request, "hospedagem/form.html", {'form': form})

def hospedagem_editar(request, id):

    hospedagem = Hospedagem.objects.get(id=id)

    if request.method == "POST":

        form = HospedagemForm(request.POST, instance=hospedagem)

        if form.is_valid():
            form.save()
            return redirect('hospedagem_listar')

    else:
        form = HospedagemForm(instance=hospedagem)

        return render(request, "hospedagem/form.html", {'form': form})

def hospedagem_remover(request, id):

    hospedagem = Hospedagem.objects.get(id=id)
    hospedagem.delete()
    return redirect('hospedagem_listar')

def hospedagem_detalhe(request, id):

    hospedagem = Hospedagem.objects.get(id=id)

    return render(request, "hospedagem/detalhe.html", {'hospedagem': hospedagem})