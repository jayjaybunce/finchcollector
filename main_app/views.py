from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Finch



# Create your views here.
def home(request):
    return render(request, 'home.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', 
    {
        'finches': finches
    }
    )

def delete_finch(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    Finch.delete(finch)
    return redirect('/finches')


def update_finch(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    if request.method == 'GET':
        return render(request, 'finches/update.html', {
            'finch' : finch,
        })
    elif request.method == 'POST':
        finch.name = name=request.POST['finch_name']
        finch.age = name=request.POST['finch_age']
        finch.color = name=request.POST['finch_color']
        finch.save()
        return redirect('/finches')

def new_finch(request):
    if request.method == 'GET':
        return render(request, 'finches/add.html')
    elif request.method == 'POST':
        finch = Finch(
            name=request.POST['finch_name'],
            color=request.POST['finch_color'],
            age=request.POST['finch_age'],

        )
        finch.save()
        return redirect('/finches')


def finches_detail(request, finch_id):
    if request.method == 'GET':
        finch = Finch.objects.get(id=finch_id)
        return render(request, 'finches/detail.html', 
        {
            'finch': finch
        }
        )

        