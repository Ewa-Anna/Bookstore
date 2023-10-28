from django.shortcuts import render

from .models import  Order, OrderItem
from .forms import OrderCreateForm

from user.models import ShippingAddress

from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = Order()
           
            if request.user.is_authenticated:
                order.user = request.user
                order.first_name = request.user.first_name
                order.last_name = request.user.last_name
                order.email = request.user.email

                most_recent_address = ShippingAddress.objects.filter(user=request.user).order_by('-updated').first()
                if most_recent_address:
                    order.street = most_recent_address.street
                    order.apartment = most_recent_address.apartment
                    order.city = most_recent_address.city
                    order.postal_code = most_recent_address.postal_code
                    order.state = most_recent_address.state
                    order.country = most_recent_address.country

            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    book=item["book"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

                cart.clear()
                return render(request, "orders/order/created.html", {"order": order})
    else:

        if request.user.is_authenticated:
            most_recent_address = ShippingAddress.objects.filter(user=request.user).order_by('-updated').first()
            initial_data = {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "street": most_recent_address.street if most_recent_address else "",
                "apartment": most_recent_address.apartment if most_recent_address else "",
                "city": most_recent_address.city if most_recent_address else "",
                "postal_code": most_recent_address.postal_code if most_recent_address else "",
                "state": most_recent_address.state if most_recent_address else "",
                "country": most_recent_address.country if most_recent_address else "",
            }
            form = OrderCreateForm(initial=initial_data)
        else:
            form = OrderCreateForm()

    return render(request, "orders/order/create.html", {"cart": cart, "form": form})
