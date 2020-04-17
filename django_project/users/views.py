from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm , ManagerForm
from .models import Manager
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def register(request):
    mform = ManagerForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            userr = User.objects.get(username = username)
            jobchoice = request.POST['jobchoices']
            if (jobchoice == '1'):
                 m = Manager.objects.create(user = userr , company = request.POST['company'])
                 m.save()
         

            messages.success(request , f"Your account has been created! You are now able to log in")
            return redirect('login')

    else:
        form = UserRegisterForm()
        
    return render(request , 'users/register.html' , {'form' : form , 'mform' : mform})

@login_required
def profile(request):
    if (request.method == 'POST'):
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f"Your account has updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request , 'users/profile.html' , context)


