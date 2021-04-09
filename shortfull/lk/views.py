

# Create your views here.
from django.shortcuts import render
from .form_lk import  Loginform
from django.contrib.auth import authenticate, login


def pagelogin(request):
    user = ''
    passwor = ''

    form = Loginform(request.POST or None)
    if form.is_valid():
        user = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            context = {'form': form,
                       'error': 'Приветствуем вас на нашей странице ! '}

            return render(request, 'lk/matroskin.html', context)
        else:



            context = {'form': form,
                       'error': 'Ошибочка в логине или пароле  ! '}
            return render(request, 'lk/login1.html', context)

    else:
        context = {'form': form}
        return render(request, 'lk/login.html', context)