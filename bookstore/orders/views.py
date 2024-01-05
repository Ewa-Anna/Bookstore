import weasyprint

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Order, OrderItem
from .forms import OrderCreateForm
from .tasks import order_created

from user.models import ShippingAddress

from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = Order()

            shipping_address, created = ShippingAddress.objects.get_or_create(
                street=form.cleaned_data["street"],
                apartment=form.cleaned_data["apartment"],
                city=form.cleaned_data["city"],
                postal_code=form.cleaned_data["postal_code"],
                state=form.cleaned_data["state"],
                country=form.cleaned_data["country"],
            )

            order = Order(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                shipping_address=shipping_address,
            )

            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount

            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    book=item["book"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            cart.clear()
            order_created.delay(order.id)  # Asynchronous task
            request.session["order_id"] = order.id
            return redirect(reverse("payment:process"))

    else:
        if request.user.is_authenticated:
            initial_data = {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
            }

            shippingaddress = ShippingAddress.objects.filter(
                user=request.user, main=True
            ).first()
            if shippingaddress:
                initial_data["street"] = shippingaddress.street
                initial_data["apartment"] = shippingaddress.apartment
                initial_data["city"] = shippingaddress.city
                initial_data["postal_code"] = shippingaddress.postal_code
                initial_data["state"] = shippingaddress.state
                initial_data["country"] = shippingaddress.country

            form = OrderCreateForm(initial=initial_data)

        else:
            form = OrderCreateForm()

    return render(request, "orders/order/create.html", {"cart": cart, "form": form})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/order/detail.html", {"order": order})


@login_required
def order_cancel(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.order_status = "canceled"
    order.save()
    return redirect("user:dashboard")


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("orders/order/pdf.html", {"order": order})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_{order.id}.pdf"
    weasyprint.HTML(string=html).write_pdf(
        response, stylesheet=[weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    )
    return response
