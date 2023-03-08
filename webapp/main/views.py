from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from .forms import UserRegistrationForm

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

def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

        else:
            for error in list(form.errors.values()):
                print(request, error)


    else:
        form = UserRegistrationForm()

    return render(
        request,
        'main/auth.html',
        context={"form": form}
    )