from django.shortcuts import render, redirect
from .models import *
from django.core import serializers
from .forms import *

# Create your views here.

def index(request):
    peta = PetaBanjir.objects.all()
    peta_json = serializers.serialize('json', peta)
    data = {
        'title' : "UAS WEBGIS IKHWAN",
        'data_peta' : peta_json,
        'petas' : peta,
        'tipss' : Tips.objects.all(),
        'i' : 1,
    }
    return render(request, 'index.html', data)

def tambahLokasi(request):
    if request.POST:
        form = FormPetaBanjir(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'Title' : 'Input data banjir',
                'form' : form,
                'Pesan' : "Data berhasil ditambahkan",
            }
            return render(request, 'tambahPeta.html', data)
    else:
        data = {
            'Title' : 'Input data banjir',
            'form' : FormPetaBanjir()
        }
    return render(request, 'tambahPeta.html', data)

def editLokasi(request, id):
    lokasiBanjir = PetaBanjir.objects.get(id = id)
    if request.POST :
        form = FormPetaBanjir(request.POST, request.FILES, instance=lokasiBanjir)
        if form.is_valid():
            form.save()
            data = {
                'Title' : 'Edit data banjir',
                'form' : form,
                'banjir' : lokasiBanjir,
                'Pesan' : "Data berhasil di ubah"
            }
            return render(request, 'updatePeta.html', data)
    else:
        data = {
            'Title' : 'Edit data banjir',
            'form' : FormPetaBanjir(instance=lokasiBanjir),
            'banjir' : lokasiBanjir
        }
    return render(request, 'updatePeta.html', data)

def hapusPeta(request, id):
    petaBanjirs = PetaBanjir.objects.get(id=id)
    petaBanjirs.delete()
    return redirect("/")

def tambahTips(request):
    if request.POST:
        form = FormTips(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'Title' : 'Input data tips',
                'form' : form,
                'Pesan' : "Data berhasil ditambahkan",
            }
            return render(request, 'tambahTips.html', data)
    else:
        data = {
            'Title' : 'Input data tips',
            'form' : FormTips()
        }
    return render(request, 'tambahTips.html', data)

def editTips(request, id):
    tips = Tips.objects.get(id = id)
    if request.POST :
        form = FormTips(request.POST, request.FILES, instance=tips)
        if form.is_valid():
            form.save()
            data = {
                'Title' : 'Edit data tips',
                'form' : form,
                'tips' : tips,
                'Pesan' : "Data berhasil di ubah"
            }
            return render(request, 'updateTips.html', data)
    else:
        data = {
            'Title' : 'Edit data tips',
            'form' : FormTips(instance=tips),
            'tips' : tips
        }
    return render(request, 'updateTips.html', data)

def hapusTips(request, id):
    tipsu = Tips.objects.get(id=id)
    tipsu.delete()
    return redirect("/")