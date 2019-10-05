from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
    'count' : count
    })

def signup(request):
    if request.user.is_authenticated:
        count = User.objects.count()
        return render(request, 'home.html', {
        'count' : count
        })
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form  = SignUpForm()
    return render(request, 'registration/signup.html', {
    'form' : form,
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')
