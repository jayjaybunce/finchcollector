from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Finch, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm, ToyForm
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# ClassBasedView here


def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('finches:index')
        else:
            error_message = 'Invalid signup - try again'

    form = UserCreationForm
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)








class FinchCreate(LoginRequiredMixin,CreateView):
    model = Finch
    fields = ['name','age','color']
    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class FinchUpdate(LoginRequiredMixin,UpdateView):
    model = Finch
    fields = ['name','color','age']


class FinchDelete(LoginRequiredMixin,DeleteView):
    model = Finch
    success_url = '/finches/'


class ToyList(LoginRequiredMixin,ListView):
    model = Toy
    




# Create your views here.
@login_required
def toys_index(request):
    toys = Toy.objects.all()
    context = {
        'toys': toys,
        'form': ToyForm(request.POST)
    }
    return render(request, 'main_app/toy_list.html', context)
@login_required
def add_toy(request):
    form = ToyForm(request.POST)
    if form.is_valid():
        new_toy = form.save()

    return redirect('finches:toys_index')

def home(request):
    return render(request, 'home.html')

@login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user)
    return render(request, 'finches/index.html', 
    {
        'finches': finches
    }
    )
@login_required
def delete_finch(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    Finch.delete(finch)
    return redirect('/finches')

@login_required
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
@login_required
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
@login_required
def add_feeding(request,finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finches:detail', finch_id=finch_id)
@login_required
def finches_detail(request, finch_id):

    finch = Finch.objects.get(id=finch_id)
    toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.values_list('id'))
    return render(request, 'finches/detail.html', 
    {
        'finch': finch,
        'toys': toys_finch_doesnt_have,
        'feeding_form': FeedingForm(request.POST),
    }
    )

@login_required
def finch_add_toy(request, finch_id, toy_id):
    toy = Toy.objects.get(pk=toy_id)
    finch = Finch.objects.get(pk=finch_id)
    finch.toys.add(toy)
    finch.save()

    return redirect('finches:detail',finch_id=finch_id)
@login_required
def finch_remove_toy(request, finch_id, toy_id):
    finch = Finch.objects.get(pk=finch_id)
    toy = Toy.objects.get(pk=toy_id)
    finch.toys.remove(toy)
    finch.save()
    return redirect('finches:detail',finch_id=finch_id)




def about(request):
    return render(request,'finches/about.html')
