from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            user = User.objects.create(name=name)
            return render(request, 'greeting.html', {'name': name})

    return redirect('home.html')


def register_api(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        if name:
            user = User.objects.create(name=name)
            return JsonResponse({'success': True, 'greeting': f'Hi {name}! Welcome to JamRoll!'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})
