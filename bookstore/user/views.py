from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Profile
from orders.models import Order
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm


@login_required
def dashboard(request):
    order_list = Order.objects.filter(email=request.user.email)
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "user/dashboard.html", {"order_list": order_list,
                                                   "profile": profile})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "user/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "user/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Successfully updated profile.")
            return redirect("dashboard")
        else:
            messages.error(request, "Profile was not updated. Error occured.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "user/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
