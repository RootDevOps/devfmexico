from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")        
        user = authenticate(username=username, password=password)
        login(request, user)
        request.session['username'] = username
        return redirect("/")
    return render(request, "login.html", {"form":form, "title":title})

def registrer_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        newuser = authenticate(username=user.username, password=password)
        login(request, newuser)
        return redirect("/")
    return render(request, "login.html", {"form":form, "title":title})

def logout_view(request):
    title = "Logout"
    form = UserLoginForm(request.POST or None)
    logout(request)
    request.session['username'] = None
    return redirect("/")

def landing_page(request):
    title = "Home"
    if request.session.get('username'):
        title = "Welcome " + request.session['username']
    return render(request, "index.html", {"title":title})
