from .models import city
from django.forms import ModelForm,TextInput, widgets

class city_form(ModelForm):
    class Meta:
        model = city
        fields = ['name']
        widgets = {'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}