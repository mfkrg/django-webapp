from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'main/index.html')

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

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Вы вошли как {username}.')
                return redirect('home')
            else:
                messages.error(request, "Неправильный логин или пароль.")
        else:
            messages.error(request, "Неправильный логин или пароль.")
    form = AuthenticationForm()
    return render(request, 'main/login.html', context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Вы успешно вышли.")
    return redirect('home')