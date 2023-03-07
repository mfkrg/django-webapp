from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
def index(request):
    return render(request, 'main/index.html')

def cart(request):
    return render(request, 'main/cart.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def about(request):
    return render(request, 'main/about.html')

def auth(request):
    return render(request, 'main/auth.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация успешна.")
            return redirect("main:index")
        messages.error(request, "Что-то пошло не так.")
    form = NewUserForm()
    return render(request=request, template_name="main/auth.html", context={"register_form":form})