from django.shortcuts import render
from .models import city
from .forms import city_form
import requests
import json
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=704ab3281f64d4068fd83d5fe9a70982'
    if request.method == "POST":
        form = city_form(request.POST)
        form.save()
    form = city_form()
    citys = city.objects.all()
    weather_data = []
    for i in citys:
        Any = requests.get(url.format(i)).json()
        city_weather = {"city":i.name,
        "temp":Any['main']['temp'],
        "description":Any["weather"][0]["description"],
        "icon":Any['weather'][0]['icon']}
        weather_data.append(city_weather)
    x = {"weather_data":weather_data,"form":form}
    return render(request,"weather/weather.html",x)