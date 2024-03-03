from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=df1bd0fafc45f5c0c64ee130445540f8').read()
        json_data = json.loads(res)
        # change json to python dictionary
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])+' '+ str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'K',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        data = {}
        city = ''
    return render(request, 'index.html', {'city': city, 'data': data})
