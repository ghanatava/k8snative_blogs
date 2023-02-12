from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):

    if request.method == "POST":
        form=UserRegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} log in now')
            return redirect('login')
    
    else:
        form = UserRegisterForm()

    return render(request,"users/register.html",{
        "form":form,
    })

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateProfileForm(request.POST,
            request.FILES,
            instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'account has been update')
            return redirect('profile')




    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateProfileForm(instance=request.user.profile)
    return render(request,"users/profile.html",{
        "u_form":u_form,
        "p_form":p_form,
    })