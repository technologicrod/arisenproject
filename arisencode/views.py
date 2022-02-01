from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm


def home(request):
    all_items = List.objects.all()
    context = {'all_items': all_items}
    return render(request, 'home.html', context)


def about(request):
    context = {'myname': 'Rodwell'}
    return render(request, 'about.html', context)


def addprof(request):
    form = ListForm(request.POST or None)
    data = List.objects.all()
    context = {"form": form, "data": data}
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    else:
        return render(request, 'addprof.html', context)


def delete(request):
    logbook = []
    all_items = List.objects.all()
    if request.method == "POST":
        dele = request.POST['dele']
        for i in all_items:
            logbook.append(i.id)
        if dele == "":
            return redirect('home')
        elif int(dele) not in logbook:
            return redirect('home')
        else:
            item = List.objects.get(pk=dele)
            item.delete()
            return redirect('home')
