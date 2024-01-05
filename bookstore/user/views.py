from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

    form = ShippingAddressForm(initial={"user": request.user.username})

    shipping_addresses = ShippingAddress.objects.filter(user=request.user)
    primary_addresses = shipping_addresses.filter(main=True)
    additional_addresses = shipping_addresses.filter(main=False)

    paginator = Paginator(order_list, 5)
    page_number = request.GET.get("page", 1)
    try:
        orders = paginator.page(page_number)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(
        request,
        "user/dashboard.html",
        {
            "orders": orders,
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

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Successfully updated profile.")
            return redirect("user:dashboard")
        else:
            messages.error(request, "Profile was not updated. Error occured.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "user/edit.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


@login_required
@require_POST
def add_shipping_address(request):
    form = ShippingAddressForm(data=request.POST, initial={"user": request.user})

    if form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user

        if form.is_duplicate():
            messages.error(request, "This shipping address already exists.")
            return render(request, "user/address.html", {"form": form})
        else:
            shipping_address.save()
            return redirect("user:dashboard")
    else:
        messages.error(request, "Postal code must be in the 00-000 format")
        form = ShippingAddressForm(initial={"user": request.user})

    return redirect("user:dashboard")


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
        return HttpResponseForbidden("You don't have permission to delete this address.")

    shipping_address.delete()

    return redirect("user:dashboard")
