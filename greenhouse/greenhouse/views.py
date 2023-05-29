from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
     
        print(username)
        # login(request, user)
        if username == 'Polyhouse' and password == 'qwerty000':
            return redirect('edit')
        else:
            messages.error(request, 'Invalid username or password.')
        

    return render(request, 'login.html')


def edit(request):
    return render(request, 'edit.html')

def graph(request):
    return render(request, 'graph.html')

def co(request):
    return render(request, 'co.html')
