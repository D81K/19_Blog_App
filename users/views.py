from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages


def register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        form.save()
    
    context = {"form": form}
    return render(request, "users/register.html", context)


def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, instance=request.user.profile, files=request.FILES)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, "Your profile has been updated")

        return redirect(request.path)
    context = {'u_form': u_form, 'p_form': p_form}
    
    return render(request, 'users/profile.html', context)