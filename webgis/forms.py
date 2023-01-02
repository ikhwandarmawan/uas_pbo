from django import forms
from .models import *

class FormPetaBanjir(forms.ModelForm):
    class Meta:
        model = PetaBanjir
        fields = '__all__'

        widgets = {
            'tanggal_mulai' : forms.DateInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'date'
                }),
            'tanggal_selesai' : forms.DateInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'date'
                }),
            'garis_lintang' : forms.NumberInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'number', 'step' : '0.000001'
                }),
            'garis_bujur' : forms.NumberInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'number', 'step' : '0.000001'
                }),
            'deskripsi' : forms.TextInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'text'
                }),
            'wilayah' : forms.TextInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'text'
                }),
            'ketinggian' : forms.NumberInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'number',
                }),
        }

class FormTips(forms.ModelForm):
    class Meta:
        model = Tips
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'text'
                }),
            'deskripsi' : forms.TextInput({
                'class':'border border-black block mb-4 rounded-lg text-black py-2 px-4', 'type' : 'text'
                }),
        }