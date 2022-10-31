from django.shortcuts import render, redirect
from app.forms import GamesForm
from app.models import Games
# Create your views here.
def home(request):
    data = {}
    data['game'] = Games.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = GamesForm
    return render(request, 'form.html', data)

def create(request):
    form = GamesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['game'] = Games.objects.get(pk=pk)
    return render(request, 'view.html', data)
def edit(request, pk):
    data = {}
    data['game'] = Games.objects.get(pk=pk)
    data['form'] = GamesForm(instance=data['game'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['game'] = Games.objects.get(pk=pk)
    form = GamesForm(request.POST or None, instance=data['game'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Games.objects.get(pk=pk)
    db.delete()
    return redirect('home')

