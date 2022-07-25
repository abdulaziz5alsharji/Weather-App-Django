from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def get_weather(request):
    city_name = request.GET.get("city_name")
    if city_name is None:
        return render(request, "weather_api/home.html", context={
        })
    API_URL = f"http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q={city_name}"
    response = requests.get(API_URL).json()
    if response["cod"] == "404":
        return HttpResponse("<h1 style='text-align:center;'>City Not Found</h1>")
    city_weather = {
        'city': city_name,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    return render(request, "weather_api/weather.html", context=city_weather)