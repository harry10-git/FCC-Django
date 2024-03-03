from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature


# Create your views here.
def index(request):
    # context = {
    #     'name': 'Harry',
    #     'age' : 21,
    #     'nationality': 'India'
    # }
    # context is dictionary 
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if(password == password2):
            # check is email is already used
            if User.objects.filter(email =email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords not same')
            return redirect('register')
    
    else: 
        return render(request, 'register.html') # render this if not post 
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else: 
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def mypost(request, pk):
    return render(request, 'mypost.html', {'pk': pk})

def counter(request):
    # text = request.POST['ta-words']
    # num_words = len(text.split())
    posts = [1,2,3,4,5,'tim', 'tom', 'john']
    return render(request, 'counter.html', {'postnames': posts})