from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.


def index(request):
    if 'user_id' not in request.session:
        return render(request, 'login/index.html')
    else:
        return redirect('books:book')


def login(request):
    # send information to model to check the errors
    if request.POST:
        valid, result = User.objects.login(request.POST)
        # if error
        if not valid:
            messages.error(request, result)
            return redirect('login:index')
        # log user in
        else:
            request.session['user_id'] = result
            messages.success(
                request, "You have been logged in successfully.")
        return redirect('books:book')
    return render(request, 'login/index.html')


def registration(request):
    errors = User.objects.basic_validation(request.POST)
    if request.POST:
        if errors:
            for error in errors:
                messages.error(request, error)
                request.session['name'] = request.POST['name']
                request.session['alias'] = request.POST['alias']
                request.session['email'] = request.POST['email']
            return redirect('login:index')
    user = User.objects.user_create(request.POST)
    request.session['user_id'] = user.id
    request.session['name'] = user.name
    messages.success(request, "You have been registered successfully.")
    return redirect('books:book')


def logout(request):
    request.session.clear()
    messages.success(request, "You have been logged out successfully.")
    return redirect('login:index')
