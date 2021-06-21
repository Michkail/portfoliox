from django.shortcuts import render

def homey(request):
  return render(request, 'homey.html')

def contactly(request):
  return render(request, 'contact.html')

def aboutly(request):
  return render(request, 'about.html')