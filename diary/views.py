from django.shortcuts import render
from dayrecords.models import Dayrecords

def main(request):
    dayrecords = Dayrecords.objects.all()
    return render(request, 'main.html', {'dayrecords':dayrecords})