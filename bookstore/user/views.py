from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

from .models import Profile, ShippingAddress
from orders.models import Order
from .forms import (
    UserRegistrationForm,
    UserEditForm,
    ProfileEditForm,
    ShippingAddressEditForm,
    ShippingAddressForm,
)


@login_required
def dashboard(request):
    order_list = Order.objects.filter(email=request.user.email)

    profile = get_object_or_404(Profile, user=request.user)
    
    form = ShippingAddressForm()

    shipping_addresses = ShippingAddress.objects.filter(user=request.user)
    primary_addresses = []  
    additional_addresses = []  

    if shipping_addresses.exists():    
        for address in shipping_addresses:
            if address.main:
                primary_addresses.append(address)
            else:
                additional_addresses.append(address)

    return render(
        request,
        "user/dashboard.html",
        {
            "order_list": order_list,
            "profile": profile,
            "shipping_addresses": shipping_addresses,
            "primary_addresses": primary_addresses,
            "additional_addresses": additional_addresses,
            "form": form,
        },
    )


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
        shipping_address_form = ShippingAddressEditForm(data=request.POST)

        if (
            user_form.is_valid()
            and profile_form.is_valid()
            and shipping_address_form.is_valid()
        ):
            user_form.save()
            profile_form.save()
            shipping_address_form.save()
            messages.success(request, "Successfully updated profile.")
            return redirect("user:dashboard")
        else:
            messages.error(request, "Profile was not updated. Error occured.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        shipping_address_form = ShippingAddressEditForm()

    return render(
        request,
        "user/edit.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "shipping_address_form": shipping_address_form,
        },
    )


@require_POST
def add_shipping_address(request):
    user = request.user
    shipping_address = None

    if request.method == "POST":
        form = ShippingAddressForm(initial={"user": request.user}, data=request.POST)

        if form.is_valid():
            if form.is_duplicate():
                messages.error(request, "This shipping address already exists.")
            else:
                shipping_address = form.save(commit=False)
                shipping_address.user = user
                shipping_address.save()
                return redirect("user:dashboard")

    else:
        form = ShippingAddressForm()

    return render(
        request,
        "user/dashboard.html",
        {"user": user, "form": form, "shipping_address": shipping_address},
    )


@login_required
def edit_shipping_address(request, shipping_address_id):
    shipping_address = get_object_or_404(ShippingAddress, pk=shipping_address_id)

    if request.user != shipping_address.user:
        return HttpResponseForbidden("You don't have permission to edit this address.")

    if request.method == "POST":
        form = ShippingAddressEditForm(request.POST, instance=shipping_address)
        if form.is_valid():
            form.save()
            return redirect("user:dashboard")
    else:
        form = ShippingAddressEditForm(instance=shipping_address)

    return render(
        request,
        "user/edit_shipping_address.html",
        {"shipping_address": shipping_address, "form": form},
    )


@login_required
def delete_shipping_address(request, shipping_address_id):
    shipping_address = get_object_or_404(ShippingAddress, pk=shipping_address_id)

    if request.user != shipping_address.user:
        return HttpResponseForbidden("You don't have permission to edit this address.")

    shipping_address.delete()

    return redirect("user:dashboard")
