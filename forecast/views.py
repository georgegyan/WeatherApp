import requests
from django.shortcuts import render
from decouple import config

def home(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '40707b12385b186a41bb1d3fb5445ac6'
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found or API error.'}

    return render(request, 'forecast/home.html', {'weather_data': weather_data})
