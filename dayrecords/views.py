from django.shortcuts import render, redirect
from .models import Dayrecords


def daily(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        dayrecords = Dayrecords(title=title, content=content)
        dayrecords.save()
        return redirect('main')
    return render(request, 'dayrecords/daily.html')
    
    
def show(request, id):
    dayrecords = Dayrecords.objects.get(pk=id)
    return render(request, 'dayrecords/show.html', {'dayrecords': dayrecords})
    
def edit(request, id):
    dayrecords = Dayrecords.objects.get(pk=id)
    return render(request, 'dayrecords/edit.html', {'dayrecords': dayrecords})
    
    
def update(request, id):
    if request.method == "POST":
        dayrecords = Dayrecords.objects.get(pk=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        dayrecords.title = title
        dayrecords.content = content
        dayrecords.save()
        return redirect('main')
        
        
def delete(request, id):
    if request.method=="POST":
        dayrecords = Dayrecords.objects.get(pk=id)
        dayrecords.delete()
        return redirect('main')
    
