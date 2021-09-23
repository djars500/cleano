from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.first_name = request.POST.get('first_name')
            new_user.last_name = request.POST.get('last_name')
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/accounts/signup/')
            # return render(request, 'main.html', {'new_user': new_user})
        else:
            messages.error(request, 'Такой пользователь существует')
            
    else:
        user_form = UserRegistrationForm()
        
        
    return render(request, 'account/register.html', {'user_form': user_form})

class SignUp(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            print(request.user)
            form = LoginForm(request.POST or None)
            return render(request, 'account/signup.html', {'form': form})        
        else:
            return redirect('/')

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/myapps/')
        else:
            form = LoginForm()
            messages.error(request, 'Неверный пароль или логин')
            

        return render(request, 'account/signup.html', {'form': form})
