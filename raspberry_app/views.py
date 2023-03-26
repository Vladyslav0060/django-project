from django.http import HttpResponse
from sense_emu import SenseHat
from django.shortcuts import render

def index(request):
    temperature = SenseHat().temp
    print('new data')
    data = {'value': temperature}
    return render(request, 'my_template.html', data)
    # return HttpResponse("Hello, world. You're at the polls index.")
    